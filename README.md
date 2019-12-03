# IronDetection
This program provides a simple web application for the SemEval 2018 Task 3: Irony Detection in English Tweets. Thanks to:   

	@InProceedings{VUN2018,
          author    = {Vu, Thanh and Nguyen, Dat Quoc and Vu, Xuan-Son and Nguyen, Dai Quoc and Catt, Michael and Trenell, Michael},
          title     = {{NIHRIO at SemEval-2018 Task 3: A Simple and Accurate Neural Network Model for Irony Detection in Twitter}},
          booktitle = {Proceedings of the 12th International Workshop on Semantic Evaluation},
          year      = {2018}
    }

and we made some modifications to the model.
## Package installation
To run the code, you need the following software packages by running **`pip install -r requirements.txt`**:
## Run the program
After the packages are installed, you can run the codes as follows:  
- `python src/new_server.py` which opens a server which can be used for binary irony (ironic vs. non-ironic) classification.  
- Open `web/index.html` in Chrome / Safari / Firefox and input the twitter to judge if it's irony.
