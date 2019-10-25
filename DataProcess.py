import numpy as np
import pandas as pd

# lec = pd.read_csv('d:/Job_dispatch/task_part_0.csv', header=None,
#                   names=['time', 'missing_info', 'job_ID', 'task_index',
#                          'machine_ID', 'even_type', 'user', 'scheduling_class', 'priority',
#                          'cpu_request', 'memory_request', 'disk_space_request',
#                          'different machines restriction'])
#
#
# lec_exp = lec.loc[:, ['time', 'job_ID', 'priority', 'cpu_request', 'memory_request']]
#
# lec_exp_nona = lec_exp.dropna(axis=0, how='any')
# lec_exp_nona = lec_exp_nona.reset_index(drop=True)
# lec_exp_nona_sample = lec_exp_nona.sample(n=5000, axis=0)
# lec_exp_nona_sample = lec_exp_nona_sample.reset_index(drop=True)
# lec_exp_nona_sample.to_csv('d:/Job_dispatch/sample.csv', index=False)
# print(lec_exp_nona_sample)

#传输时间,10个edge server

# tran_10server = pd.DataFrame(columns=[0,1,2,3,4,5,6,7,8,9])
#
# for i in range(5000):
#     tran_speed = [np.random.uniform(low=0.2, high=0.4, size=None) for x in range(10)]
#     for r in range(10):
#         tran_10server.loc[i,r]=tran_speed[r]
#
# tran_10server.to_csv('d:/Job_dispatch/10sever_speed.csv', index=False)
#


process_ener = pd.DataFrame(columns=['pt_local','pt_edge','ener_tran','ener_local'])

for i in range(5000):

    process_ener.loc[i,'pt_local']=np.random.uniform(low=0.2, high=0.4, size=None)
    process_ener.loc[i,'pt_edge'] = np.random.uniform(low=0.1, high=0.2, size=None)
    process_ener.loc[i,'ener_tran'] = np.random.uniform(low=0.4, high=0.5, size=None)
    process_ener.loc[i,'ener_local'] = np.random.uniform(low=0.5, high=0.6, size=None)

process_ener.to_csv('d:/Job_dispatch/process_ener.csv', index=False)







#print(np.random.uniform(low=0.2, high=0.4, size=None))
# tran_speed = [np.random.uniform(low=0.2, high=0.4, size=None) for x in range(10)]
# serverse_speed = pd.Series(tran_speed, index=[x for x in range(10)])
# print(tran_speed)
# lec_exp_nona.loc[0, 'transaction time'] = tran_speed
# print(lec_exp_nona)
# lec_exp_nona_sample = lec_exp_nona.sample(n=5000, axis=0)
#
# lec_exp_nona_sample = lec_exp_nona_sample.reset_index(drop=True)
#
# for i in range(0, 10):
#        tran_speed = [np.random.uniform(low=0.2, high=0.4, size=None) for x in range(10)]
#        serverse_speed = pd.Series(tran_speed, index=[x for x in range(10)])
#        lec_exp_nona_sample.loc[i, 'transaction time'] = serverse_speed
#
# lec_exp_nona_sample.to_csv('d:/Job_dispatch/sample.csv', index=False)
#
# print(lec_exp_nona_sample)