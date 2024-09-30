I wanted to learn how a PINN worked, and how it differs from a  normal neural network. For this project i followed the work done by Theo Wolf in his article i have linked here.

To begin, i had to implement the network itself. This is done in the file network. The implementation of this network was surprisingly close to that of a normal network,as the PINN differs only in the loss we use. This network file is flexible enough to be used as both a PINN and a regular neural network, depending on the choice of loss we pass to it.

As mentioned above, the difference with the PINN comes from not just evaluating its loss with respect to the data itself, but to its theoretically derived governing equation. The uniqueness of this is the solution to the governing equations doesn't need to be known. This allows us to model a procedss as a diferential equation, take some data, and then fit the equation itself to the data and evaluate. 
A further improvement i will make to this project, following what Theo Wolf did, is implement a function that allows us to find the value of certain constants from this fitting process. For example, he was able to find the cooling rate r by modelling a cooling cup of coffee with Newtons Law of Cooling. Althouhg in this toy example he could have solved the ODE and fitted the theoretical solution and found a similiar value for r, this is not an option in many more complicated cases.

I found this project to be particularly useful as it has greatly increased my depth of understanding of how neural networks work, how to best program them, and how they can be tweaked to provide additional information - for example using the editted loss function to create a PINN.

With thanks to @theo.wolf

https://medium.com/@theo.wolf/physics-informed-neural-networks-a-simple-tutorial-with-pytorch-f28a890b874a
