print 'Let\'s get started!'

spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")
print 'Welcome' + spy_name + '.Glad to have you back with us.'
spy_salutation = raw_input('What should  we call you (MR. or MS.)?')
spy_salutation  +' '+ spy_name
spy_name = spy_salutation +' '+ spy_name
print spy_name


if len(spy_name) > 0:
    # Start writing from here now. See how this is under the if statement?


    print 'Welcome ' + spy_name + '. Glad to have you back with us.'

    spy_salutation = raw_input("Should I call you Mister or Miss?: ")

    spy_name = spy_salutation + " " + spy_name

    print "Alright " + spy_name + ". I'd like to know a little bit more about you before we proceed..."
else:

            print "A spy needs to have a valid name. Try again please."