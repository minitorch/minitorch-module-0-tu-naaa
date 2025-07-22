### 1 NN
Neural networks are compound model classes that divide classification into two or more stages.

Each stage uses a linear model to seperate the data. And then an activation function to reshape it.

<img width="250" height="250" alt="image" src="https://github.com/user-attachments/assets/72d8591c-1eba-4a34-9ca0-eaa0f8bad819" />
<img width="250" height="250" alt="image" src="https://github.com/user-attachments/assets/9f637297-2bab-4090-9939-fd70aeaf1ecc" />

Using ReLU activating function:

<img width="350" height="200" alt="image" src="https://github.com/user-attachments/assets/52118a13-a9d4-41e4-b715-dba1874b74fa" />
<img width="350" height="200" alt="image" src="https://github.com/user-attachments/assets/ae0c92bf-3fde-43dc-beb6-ecf6b0ec650b" />

Basically the right X's are thresholed to positive values and the other O's and X's are 0.

Since all the O's are now at the origin it is very easy to separate out the space:

<img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/626e6b7a-7129-4f9b-b38d-f7cd3335322e" />

Mathematically, we can understand it this way:

<img width="600" height="125" alt="image" src="https://github.com/user-attachments/assets/b4ff97d7-79a8-4709-bc47-06239ac1a97b" />

