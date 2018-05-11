##Quando fai il fit, dumpa la feature importance
self.bdt[provider_str].fit(X_train_mdl.astype(np.float32),
                           np.squeeze(y_train_mdl).astype(np.float32))
filename='feature_importance_ITA.p'
##Preparo ora un bel dizionario
dict={}
dict['feature_importance']=self.bdt[provider_str].feature_importances_
dict['feature'] = []
for col in X_train_mdl.columns:
    dict['feature'].append(col)

pickle.dump(dict, open(filename,'wb'))



import pickle
dict = pickle.load(open('feature_importance_ITA.p','rb'))
snow_importance=[]
index = []
for i in range(len(dict['feature'])):
    if 'sd' in dict['feature'][i]:
        print(i,dict['feature'][i],dict['feature_importance'][i])
        snow_importance.append(dict['feature_importance'][i])
        index.append(i)


import matplotlib.pyplot as plt
plt.figure()

plt.plot(index, snow_importance,color='r',label='feature_importance')
plt.legend(loc='upper right')
plt.show()
#plt.close()   
