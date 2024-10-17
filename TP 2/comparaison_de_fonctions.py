import time 

def f(t : int) :
    tab = []
    for a in [1000*60*60*24*30*365,1000*60*60*24*30,1000*60*60*24,1000*60*60,1000*60,1000] :
        q,r=divmod(t,a)
        tab.append(q)
        t=t-q
    return tab

# t_0 = time.time()
# print(f())
# t_1 = time.time()
# ellapsed_time = t_1-t_0
# runtime_conversions = f(ellapsed_time)
runtime_conversions = f(time.time())
print(f'{runtime_conversions[0]} annees,{runtime_conversions[1]} mois, {runtime_conversions[2]} jours,{runtime_conversions[3]}  heures, {runtime_conversions[4]} minutes, {runtime_conversions[5]} secondes')