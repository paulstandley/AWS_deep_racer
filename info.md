# INFO

1 In your AWS account, go to the Management Console. (You can also directly sign in to the AWS DeepRacer Console in the upper-right here, which skips the next couple of steps).

2 Choose the us-east-1 (N. Virginia) region at the top right corner of the Regions dropdown menu.

3 From the top left of the console, click Services, type DeepRacer in the search box, and select AWS DeepRacer. That will open the AWS DeepRacer console.

4 On the landing page, if it is your first time visiting AWS DeepRacer, you may need to select Get Started, and then Create Resources to provision the necessary AWS resources. Otherwise, you can click Create model.

5 Create a model name and description.

6 Under Environment simulation, select a track from the list. It’s recommended to start with the “re:Invent 2018 Track” and then explore more tracks from there.
7 Under Action space, familiarize yourself with these settings and accept the defaults.

8 Read through the default (basic) reward function and check out the other examples. Note that you will want to “validate”if you update the default in the future.

9 Expand Hyperparameters to review the different hyperparameters available to set. For this exercise, accept the default hyperparameter settings.

10 For the Stop conditions go ahead and choose a max time of 60 minutes and click Start training.

11 The training section will allow you to see the reward function over time, as well as see a live stream of the simulator. Note that you may need to re-load the page if the stream does not update. Select the name of the model to watch the live stream in the simulator. Notice how your car is moving and become familiar with the general look and feel of the simulation. The new training will initiate in about 6 minutes. You then must wait for the training job to complete before proceeding. If you choose a maximum time of 60 minutes, it will take up to 60 minutes for this training job to complete. It is complete when the status reads “Ready.” Note: Since the training job may take more than an hour, you might want to consider moving on to the next lesson of this course while the training job is running.

12 Now, select the name of the model you just trained and click Start evaluation (*Note: You can also click on Reinforcement Learning on the left to get either your trained model or some pre-trained sample models to evaluate. Click on the name, then Start new evaluation).

13 Select the same track you used for training.

14 Set the number of trials to 3 and click Start evaluation. The evaluation results will update in approximately 5 minutes.

15 Before the evaluation job completes, take some time to watch the simulator to see how your car’s performing in real time. Look for things that you might want to tweak in the future and note them down. You’ll have a chance to apply some of those ideas in a later exercise in the course.

16 Watch the evaluation results update and write them down. You will use your results from this model as a benchmark that you can compare to as you tweak your model in later exercises.
