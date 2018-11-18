
name=input('Enter your best girl friend Name')
age=int(input("Enter Age of "+name))
hobby=input('Enter a Hobby common with you both')
frnd_year=int(input("how may years u are friend with "+name))
myAge=int(input('What\'s your age?'))
def ageDiff(age,myAge):
    if age==myAge:
        return 'even we are of same age.'
    elif age>myAge:
        return 'even I am younger than her.'
    else:
        return 'even I am elder than her.'

print('\n\n\n*******Here is Your Story*******\n\n')

print(name.title()+" is aged "+str(age)+".\nWe had a mutual hobby as "+hobby+', we were loved to do that. We spent most of ou times in this. This is the main reson we are friends till '+str(frnd_year)+' years.\nOur friendship bond is very closer '+ageDiff(age,myAge)+'\n\n\n*******End*******')