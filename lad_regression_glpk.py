import glpk
##M is a pandas dataframe
##M contains competing models, last column of ones, the target variable (actuals)
target='Actual'
#########
b=M[[target]]
M=M.drop([target],axis=1)
p=len(M.columns.values) ##length of available models + bias
n=len(b)                ##length of observed values

##Inserting identity matrices, ones and zeros where needed
dfI_u = pd.DataFrame(np.eye(n, n),
                     index=M.index.values,
                     columns=['u' for x in (range(n))])
dfI_v = pd.DataFrame(-np.eye(n, n),
                     index=M.index.values,
                     columns=['v' for x in (range(n))])
M=pd.concat([M,dfI_u,dfI_v],axis=1)
cols=[1 for m in range(p-1)] + [0 for m in range(p-1,len(M.columns.values))]

M.loc[M.index.values[-1]+1] = cols
M.loc[M.index.values[-1]+1] = cols
b.loc[b.index.values[-1]+1] = 1
b.loc[b.index.values[-1]+1] = 1
#obj function to minimize
f=[0 for m in range(p)] + [1 for m in range(p,len(M.columns.values))]
#print(M)
#print(b)
#print(f)
##Solve the linear system
lp = glpk.LPX()             
lp.name = 'optimization'     
lp.obj.maximize = False  #minimization problem    

#Define the incognitae
lp.cols.add(len(M.columns.values))         
##Bounds on incognitae 
i=0
for x in lp.cols:      #Iterate over all columns
    x.name = 'x%d' % x.index # Name them x0, x1, x2,...
    if i<p-1:
        x.bounds = 0.0, 1        # Set bound 0 <= xi < 1
    elif i==p-1:
        x.bounds = None, None     # Intercept has no bound
    else:
        x.bounds = 0, None        # u and vs positive
    #print(x.name,x.bounds)
    i+=1

##Constraints (row by row of the M matrix)
lp.rows.add(len(M))
for const in range(len(M)):
    #equality constraints: so same up and lw bounds
    lp.rows[const].bounds = b.iloc[const].values[0],b.iloc[const].values[0]

##Define the problem
lp.obj[:] = f
list=np.concatenate(M.values, axis=0 )
lp.matrix = list
##Solve the system
lp.simplex() 

##Solution
sol=[]
for c in lp.cols:
    #if i<p: #only the first p coefficients are important to us
    #print(c.name,c.primal)
    sol.append(c.primal)

##cook the final blend
if df.loc[df['valuedate']==valuedate,NN_model].values[0]*df.loc[df['valuedate']==valuedate,SUPSI_model].values[0] ==0:
    df.loc[df['valuedate']==valuedate,'lad_blend']= sol[0]*df.loc[df['valuedate']==valuedate,NN_model] +\
                                                    sol[1]*df.loc[df['valuedate']==valuedate,SUPSI_model]
else:
    df.loc[df['valuedate']==valuedate,'lad_blend']= sol[0]*df.loc[df['valuedate']==valuedate,NN_model] +\
                                                               sol[1]*df.loc[df['valuedate']==valuedate,SUPSI_model] +\
                                                               sol[2]

##PostProcess to be added: if <0 put 0, if > dispatch, put dispatch
