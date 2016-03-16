import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

csvfilename_lst = ['Test_13621.txt', 'Test_13659.txt', 'Test_13685.txt', 'Test_9886.txt', 'Test_6524.txt', 'Test_11483.txt', ]

# data = pd.read_csv(csvfilename, usecols = ["trialNo", "Filename", "pos_x", "pos_y", "currentTime"], header = 0)
# a list of practice 6 pieces music wav files
filenameList_prac = ['C:\\Calibration\\Spring.wav', \
                'C:\\Calibration\\Elan.wav', \
                'C:\\Calibration\\Sestetto.wav', \
                'C:\\Calibration\\BaileroWav.wav', \
                'C:\\Calibration\\RichterWav.wav', \
                'C:\\Calibration\\Schoenberg_PierrotLunaire.wav']

# a list of pieces music wav files for test
filenameList= [ 'C:\\Calibration\\Brahms.wav', \
                'C:\\Calibration\\Totentanz.wav', \
                'C:\\Calibration\\TubaMirum.wav', \
                'C:\\Calibration\\Spiegel.wav', \
                'C:\\Calibration\\Nimrod.wav', \
                'C:\\Calibration\\Tristan.wav', \
                'C:\\Calibration\\Figaro.wav', \
                'C:\\Calibration\\DieWalkure.wav', \
                'C:\\Calibration\\Widmung.wav', \
                'C:\\Calibration\\Rameau.wav', \
                'C:\\Calibration\\Monteverdi.wav', \
                'C:\\Calibration\\Omyson.wav', \
                'C:\\Calibration\\Threnody.wav', \
                'C:\\Calibration\\DiesIrae.wav', \
                'C:\\Calibration\\Cosi.wav', \
                'C:\\Calibration\\AdagioBarber.wav', \
                'C:\\Calibration\\Osoavefanciulla.wav', \
                'C:\\Calibration\\Lakme.wav']


######################################################################################

# Data Initialization and data structure definition
######################################################################################
# initialization for mouse location
x = np.array([])
y = np.array([])
z = np.array([])

num = 0
title = ""

# initialization a dictionary of pieces music (for subtotal per music)
dict_music = {}
for file in filenameList:
    dict_music[file] = [x, y, num, title]
# initialization for practice music dictionary
dict_music_prac = {}
for file in filenameList_prac:
    dict_music_prac[file] = [x, y, num, title]

# initial a dictionary for testers
dict_tester = {}
for filename in csvfilename_lst:
    dict_tester[filename] = [x, y, num, title]

dict_tester_prac = {}
for filename in csvfilename_lst:
    dict_tester_prac[filename] = [x, y, num, title]
# initial a dictionary of music and tester

dict_mu_te = {}
num_tester = 0
for filename in csvfilename_lst:
    dict_mu_te[filename] = [{}, num_tester]
    for file in filenameList:
        dict_mu_te[filename][0][file] = [x, y, z, num, title]

dict_mu_te_prac = {}
for filename in csvfilename_lst:
    dict_mu_te_prac[filename] = [{},num_tester]
    for file in filenameList_prac:
        dict_mu_te_prac[filename][0][file] = [x, y, z, num, title]


# data list for all tester and music GrandTotal
list_all = [x, y]


#########################################################################################################

#Import Data to the defined data structure

####################################################################################################

num_tester = 0
num_mu_te = 0
num_mu_te_prac = 0
for filename in csvfilename_lst:
    data = pd.read_csv(filename, header=0, delim_whitespace=True)
    # data = pd.read_csv('Test_mk.csv', index_col= "Filename")



    print(data.shape)
    print(data.columns)

    trialNoList = pd.unique(data.trialNo.ravel())
    fileList = pd.unique(data.Filename.ravel())

    # putdata to tester dictionary
    dict_tester[filename][0] = data.loc[data['type'].isin(['experiment'])].ix[:, 'pos_x'].values
    dict_tester[filename][1] = data.loc[data['type'].isin(['experiment'])].ix[:, 'pos_y'].values

    dict_tester[filename][2] = num_tester
    dict_tester[filename][3] = filename.split('.')[0]

    dict_tester_prac[filename][0] = data.loc[data['type'].isin(['practice'])].ix[:, 'pos_x'].values
    dict_tester_prac[filename][1] = data.loc[data['type'].isin(['practice'])].ix[:, 'pos_y'].values

    dict_tester_prac[filename][2] = num_tester
    dict_tester_prac[filename][3] = filename.split('.')[0]

    #put all x y to list_all
    list_all[0] = np.append(list_all[0], data.ix[:, 'pos_x'].values)
    list_all[1] = np.append(list_all[1], data.ix[:, 'pos_y'].values)

    dict_mu_te_prac[filename][1] = num_tester
    dict_mu_te[filename][1] = num_tester




    num_tester += 1









    # put data to music dictionary
    num_music = 0
    for file in filenameList:

        dict_music[file][0] = np.append(dict_music[file][0],data.loc[data['Filename'].isin([file])].ix[:, 'pos_x'].values)
        dict_music[file][1] = np.append(dict_music[file][1],data.loc[data['Filename'].isin([file])].ix[:, 'pos_y'].values)
        title = file.split('\\')[-1]
        dict_music[file][2] = num_music
        dict_music[file][3] = title



        dict_mu_te[filename][0][file][0] = data.loc[data['Filename'].isin([file])].ix[:, 'pos_x'].values
        dict_mu_te[filename][0][file][1] = data.loc[data['Filename'].isin([file])].ix[:, 'pos_y'].values
        dict_mu_te[filename][0][file][2] = data.loc[data['Filename'].isin([file])].ix[:, 'CurrentTime'].values - data.loc[data['Filename'].isin([file])].ix[:, 'StartTime'].values
        dict_mu_te[filename][0][file][3] = num_music
        dict_mu_te[filename][0][file][4] = file.split('\\')[-1]

        num_music += 1







    # pull out data to practice music dictionary
    num_music_prac = 0
    for file in filenameList_prac:

        dict_music_prac[file][0] = np.append(dict_music_prac[file][0],data.loc[data['Filename'].isin([file])].ix[:, 'pos_x'].values)
        dict_music_prac[file][1] = np.append(dict_music_prac[file][1],data.loc[data['Filename'].isin([file])].ix[:, 'pos_y'].values)


        title = file.split('\\')[-1]

        dict_music_prac[file][2] = num_music_prac
        dict_music_prac[file][3] = title

        dict_mu_te_prac[filename][0][file][0] = data.loc[data['Filename'].isin([file])].ix[:, 'pos_x'].values
        dict_mu_te_prac[filename][0][file][1] = data.loc[data['Filename'].isin([file])].ix[:, 'pos_y'].values
        dict_mu_te_prac[filename][0][file][2] = data.loc[data['Filename'].isin([file])].ix[:, 'CurrentTime'].values - data.loc[data['Filename'].isin([file])].ix[:, 'StartTime'].values
        dict_mu_te_prac[filename][0][file][3] = num_music_prac
        dict_mu_te_prac[filename][0][file][4] = file.split('\\')[-1]

        num_music_prac += 1



########################################################################################
# The following are plots
# by commenting out, you choose the figures you like to see

#######################################################################################


"""

## draw heat map for each music and tester


for key in dict_mu_te_prac:
    f, axarr = plt.subplots(2, 3,  sharex = True, sharey = True)
    for key1 in dict_mu_te_prac[key]:
        ax = axarr[divmod(dict_mu_te_prac[key][key1][3], 3)[0],divmod(dict_mu_te_prac[key][key1][3],3)[1]]
        sns.kdeplot(dict_mu_te_prac[key][key1][0], dict_mu_te_prac[key][key1][1], shade=True, cmap="Reds", ax = ax)
        ax.set_title(dict_mu_te_prac[key][key1][4])
        ax.set_xlim(-400, 400)
        ax.set_ylim(-350, 350)

    plt.suptitle(key.split('.')[0])
    plt.show()
    f.savefig(key.split('.')[0]+'heatmapPractice.pdf')
    plt.close(f)



for key in dict_mu_te:
    f1, axarr = plt.subplots(6, 3,  sharex = True, sharey = True)
    for key1 in dict_mu_te[key]:
        ax = axarr[divmod(dict_mu_te[key][key1][3], 3)[0],divmod(dict_mu_te[key][key1][3],3)[1]]
        sns.kdeplot(dict_mu_te[key][key1][0], dict_mu_te[key][key1][1], shade=True, cmap="Reds", ax = ax)
        ax.set_title(dict_mu_te[key][key1][4])
        ax.set_xlim(-400, 400)
        ax.set_ylim(-350, 350)

    plt.suptitle(key.split('.')[0])
    plt.show()
    f1.savefig(key.split('.')[0]+'heatmapByMusic.pdf')
    plt.close(f1)

# plot subtotal heatmap  per person


f_pt, axarr = plt.subplots(2, 3,  sharex = True, sharey = True)
for key in dict_tester:

    ax = axarr[divmod(dict_tester[key][2], 3)[0],divmod(dict_tester[key][2],3)[1]]
    sns.kdeplot(dict_tester[key][0], dict_tester[key][1], shade=True, cmap="Reds", ax = ax)
    ax.set_title(dict_tester[key][3])
    ax.set_xlim(-400, 400)
    ax.set_ylim(-350, 350)

plt.suptitle('heatmap By Tester')
plt.show()
f_pt.savefig('heatmapbytester.pdf')
plt.close(f_pt)


f_pt1, axarr = plt.subplots(2, 3,  sharex = True, sharey = True)
for key in dict_tester_prac:

    ax = axarr[divmod(dict_tester_prac[key][2], 3)[0],divmod(dict_tester_prac[key][2],3)[1]]
    sns.kdeplot(dict_tester_prac[key][0], dict_tester_prac[key][1], shade=True, cmap="Reds", ax = ax)
    ax.set_title(dict_tester_prac[key][3])
    ax.set_xlim(-400, 400)
    ax.set_ylim(-350, 350)

plt.suptitle('Heatmap By Tester Practice')
plt.show()
f_pt1.savefig('heatmapbytesterPractice.pdf')
plt.close(f_pt1)



#plot subtotal heatmap per music
f_pm, axarr = plt.subplots(2, 3,  sharex = True, sharey = True)

for key in dict_music_prac:
    ax = axarr[divmod(dict_music_prac[key][2], 3)[0],divmod(dict_music_prac[key][2],3)[1]]
    sns.kdeplot(dict_music_prac[key][0], dict_music_prac[key][1], shade=True, cmap="Reds", ax = ax)
    ax.set_title(dict_music_prac[key][3])
    ax.set_xlim(-400, 400)
    ax.set_ylim(-350, 350)

plt.suptitle('subTotal by practice music')
plt.show()
f_pm.savefig('ByMusic_heatmapPractice.pdf')
plt.close(f_pm)


f_pm1, axarr = plt.subplots(6, 3,  sharex = True, sharey = True)

for key in dict_music:
    ax = axarr[divmod(dict_music[key][2], 3)[0],divmod(dict_music[key][2], 3)[1]]
    sns.kdeplot(dict_music[key][0], dict_music[key][1], shade=True, cmap="Reds", ax = ax)
    ax.set_title(dict_music[key][3])
    ax.set_xlim(-400, 400)
    ax.set_ylim(-350, 350)

plt.suptitle('subTotal by music')
plt.show()
f_pm1.savefig('ByMusic_heatmap.pdf')
plt.close(f_pm1)
"""
#plot trajectory



#for key in dict_mu_te_prac['Test_13621.txt']:

f_tr, axarr = plt.subplots(2, 3, sharex = True, sharey = True,  subplot_kw = {'projection':'3d'})
for filename in csvfilename_lst:

    #key1s = filenameList_prac[[0,1]]
    #for key1 in key1s:
    for file in filenameList_prac:
        #ax[dict_mu_te_prac[key][key1][3]] = f_tr.add_subplot(2,3,dict_mu_te_prac[key][key1][3]+1, projection ='3d')
        ax = axarr[divmod(dict_mu_te_prac[filename][1], 3)[0],divmod(dict_mu_te_prac[filename][1],3)[1]]
        ax.plot(dict_mu_te_prac[filename][0][file][0], dict_mu_te_prac[filename][0][file][1], dict_mu_te_prac[filename][0][file][2]/1000, '-b')
        ax.set_xlim(-400, 400)
        ax.set_ylim(-350, 350)
        ax.set_zlim(0, 80)
        #plt.hold(True)

plt.suptitle('TrajectoryPractice')
plt.show()
f_tr.savefig('TrajectoryPractice.pdf')
plt.close(f_tr)




f_tr1, axarr = plt.subplots(2, 3, sharex = True, sharey = True,  subplot_kw = {'projection':'3d'})
for filename in csvfilename_lst:

    #key1s = filenameList_prac[[0,1]]
    #for key1 in key1s:
    for file in filenameList:
        #ax[dict_mu_te_prac[key][key1][3]] = f_tr.add_subplot(2,3,dict_mu_te_prac[key][key1][3]+1, projection ='3d')
        ax = axarr[divmod(dict_mu_te[filename][1], 3)[0],divmod(dict_mu_te[filename][1],3)[1]]
        ax.plot(dict_mu_te[filename][0][file][0], dict_mu_te[filename][0][file][1], dict_mu_te[filename][0][file][2]/1000, '-b')
        ax.set_xlim(-400, 400)
        ax.set_ylim(-350, 350)
        ax.set_zlim(0, 80)
        #plt.hold(True)


plt.suptitle('Trajectory')
plt.show()
f_tr1.savefig('Trajectory.pdf')
plt.close(f_tr1)

# plot usage of mouse for all user grand-Total
f_t = plt.figure()
ax = plt.axes(xlim=(-400, 400), ylim = (-350, 350))

sns.kdeplot(list_all[0], list_all[1], shade=True, cmap="Reds", ax=ax)
plt.suptitle('mouse movement')
plt.show()

# f.savefig(csvfilename.split('.')[0]+'.pdf')
f_t.savefig('total.pdf')

