import imageio
images = ['wclock.png' , 'chest.png']
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('/Users/safinah/projects/curiosity_measure_app/clock.gif', images)