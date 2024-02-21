import random
lowercharacters = "abcdefghijklmnopqrstuvwxyz";
uppercharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
numbers = "0123456789";
symbols = "1@#$%^&*()?/";
all = lowercharacters+uppercharacters+numbers+symbols;

length = 8;
password = "".join(random.sample(all,length));
print("enter 8 digit password")
print("You password is: " + password);