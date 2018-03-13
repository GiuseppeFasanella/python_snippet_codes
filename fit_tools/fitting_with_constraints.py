###Da sistemare

x = data[:,0]
y = data[:,1]
        
        def polynomial(p, x):
            return p[0]+p[1]*x+p[2]*x**2+p[3]*x**3
    
    #     def constraint_2nd_der(p):
    #         return -(2*p[2]+6*p[3]*x)
    
        def constraint_1st_der(p):
            return -(p[1]+2*p[2]*x+3*p[3]*x**2)
    
        def objective(p):
            return ((polynomial(p, x)-y)**2).sum()
    
    
    #     cons = (dict(type='ineq', fun=constraint_1st_der), dict(type='ineq', fun=constraint_2nd_der))
        cons = (dict(type='ineq', fun=constraint_1st_der))
        res = minimize(objective, x0=np.array([0, 0, 0, 0]), method='SLSQP', constraints=cons, options={'maxiter': 1000, 'disp': False})
    #     if res.success:
    #         pars = res.x
    #         xfit = np.linspace(x.min(), x.max(), 100)
    #         pol = polynomial(pars, xfit)
    #         plt.plot(x, y, 'x', xfit, pol, '-')
    #         plt.show()
    #     else:
    #         print('Failed')
    
        fit_coeffs[hh,:,dd]=res.x
