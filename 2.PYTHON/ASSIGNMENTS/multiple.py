
class multiplefunction():
    def oddeven():
        num=int(input("enter the number:"))
        if((num%2)==1):
            print("odd number")
            message="odd number"
        else:
            print("even number")
            message="even number"
        return message
    def bmi():
        bmi=int(input("enter the value"))
        if(bmi<18.5):
            print("underweight")
            message="underweight"
        elif(bmi<24.9):
            print("normal")
            message="normal"
        elif(bmi<29.9):
            print("over weight")
            message="overweight"
        else:
            print("very overweight")
            message="overweight"
        return message  