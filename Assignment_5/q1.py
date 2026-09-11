import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x=np.array([0.5,0.8,1.5,2.1,5.4,3.2,1.8,0.9,2.2,0.7,4.3,3.8,4.7,6.4,4.1,3.1,2.7,1.6,0.6,1.1])
y=np.array([5.12,7.06,8.65,11.78,26.37,19.91,10.57,7.39,10.99,9.36,22.35,22.30,24.08,29.91,20.25,18.53,15.25,11.04,7.25,10.08])
n=len(x)

x_m=np.mean(x)
y_m=np.mean(y)
s_xx=np.sum((x-x_m)**2)
s_xy=np.sum((x-x_m)*(y-y_m))

m_val=s_xy/s_xx
c_val=y_m-m_val*x_m
y_p=m_val*x+c_val
res=y-y_p

var_res=np.sum(res**2)/(n-2)
r_sq=1-(np.sum(res**2)/np.sum((y-y_m)**2))

print("(a) Regression Parameters")
print("Slope:",round(m_val,4))
print("Intercept:",round(c_val,4))
print("Variance_of_Residuals:",round(var_res,4))

print("\n(d) Coefficient of Determination")
print("R_Squared:",round(r_sq,4))

x_new=7.0
y_new=m_val*x_new+c_val
t_val=stats.t.ppf(0.95,n-2)
se_mean=np.sqrt(var_res*(1/n+((x_new-x_m)**2)/s_xx))
ci_low=y_new-t_val*se_mean
ci_high=y_new+t_val*se_mean

print("\n(e) Prediction & Interval")
print("Predicted_y_at_x=7:",round(y_new,4))
print("90%_Confidence_Interval:[",round(ci_low,4),",",round(ci_high,4),"]")


plt.figure(figsize=(6,4))
plt.scatter(x,res)
plt.axhline(0,color='red',linestyle='--')
plt.title("Residuals vs X (Independence)")
plt.xlabel("X")
plt.ylabel("Residuals")
plt.tight_layout()
plt.savefig("Residuals_vs_X",dpi=300)
plt.show()


plt.figure(figsize=(6,4))
plt.hist(res,bins=6,edgecolor='black')
plt.title("Histogram of Residuals (Distribution)")
plt.xlabel("Residual Value")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("Histogram_of_Residuals",dpi=300)
plt.show()
