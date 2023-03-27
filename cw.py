#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

#Any code taken from other sources is referenced within my code solution.

#Student ID: 20210007

#Westminster ID: w1912783 

#Date: 11/04/2022


#Creating Variables
pro_count=0
pro_m_t_count=0
no_progress=0
exclude_count=0
progress_list=[]
trailer_list=[]
retriver_list=[]
exclude_list=[]

#Horizontal Histogram
def h_histo():
    print("------------------------------------------------------------------")
    print("Horizontal Histogram")
    print("Progress ",pro_count,":",end=" ")  
    for c in range(0,pro_count):
        print("*",end=" ")
    print()
    print("Trailer  ",pro_m_t_count,":",end=" ")
    for y in range(0,pro_m_t_count):
        print("*",end=" ")
    print()
    print("Retriver ",no_progress,":",end=" ")
    for z in range(0,no_progress):
        print("*",end=" ")
    print()
    print("Excluded ",exclude_count,":",end=" ")
    for i in range(0,exclude_count):
        print("*",end=" ")
    print()
    t_o = pro_count + pro_m_t_count + no_progress + exclude_count
    print(t_o,"outcomes in total")
    
    print("------------------------------------------------------------------")

#Vertical Histrogram
def v_histo():
    print("------------------------------------------------------------------")
    print("Vertical Histogram")
    print("progress",pro_count," Trailer",pro_m_t_count," Retriver",no_progress," Excluded",exclude_count)
    for x in range(max(pro_count,pro_m_t_count,no_progress,exclude_count)):
        print( "    {0}          {1}           {2}          {3}".format( 
            '*' if x < pro_count else ' ',
            '*' if x < pro_m_t_count else ' ',
            '*' if x < no_progress else ' ',
            '*' if x < exclude_count else ' '
            ))
    #referenced this code-stack overflow(the website),Searched how do i make "*" print vertically on python loops?,answered by boonwj
    #link- https://stackoverflow.com/questions/53285446/how-do-i-make-print-vertically-on-python-loops
    print()
    t_o = pro_count + pro_m_t_count + no_progress + exclude_count
    print(t_o,"outcomes in total")
        
    print("-------------------------------------------------------------------")

#Progression list
def progression_list():
    for w in progress_list:
        print("Progress -",w)
        
    for h in trailer_list:
        print("Trailer -",h)
    
    for a in retriver_list:
        print("Retriver -",a)
    
    for b in exclude_list:
        print("Exclude _",b)

#Progression text file
def text_file():
    mod_f=open("Cw_t.txt","w")
    
    for w in progress_list:
        mod_f.write("Progress -")
        mod_f.write(str(w))
        mod_f.write(" ")
        mod_f.write("\n")
        
    for h in trailer_list:
        mod_f.write("Trailer -")
        mod_f.write(str(h))
        mod_f.write(" ")
        mod_f.write("\n")
    
    for a in retriver_list:
        mod_f.write("Retriver  -")
        mod_f.write(str(a))
        mod_f.write(" ")
        mod_f.write("\n")

    for b in exclude_list:
        mod_f.write("Exclude -")
        mod_f.write(str(b))
        mod_f.write(" ")
        mod_f.write("\n")

    mod_f.close()
#main version
def main_version():
    global option,pro_count,pro_m_t_count,no_progress,exclude_count
    print("Enter 1------>Student version \nEnter 2------>Staff Version ")
    module_opt=int(input("Enter the number between 1 to 2: "))
    #THE STUDENT VERSION
    if module_opt==1:
        print("Student Version with Histogram")
        print()
        option="Y"
        while option=="y" or option=="Y":
            try:
                pas=int(input("Please enter your credits at pass: ")) 
                if not 0<=pas<=120 or pas%20!=0:  
                    print("Out of range") 
                    continue 
                defer=int(input("Please enter your credit at defer: "))
                if not 0<=defer<=120 or defer%20!=0:   
                    print("Out of range")  
                    continue 
                fail=int(input("Please enter your credit at fail: "))
                if not 0<=fail<=120 or fail%20!=0: 
                    print("Out of range")  
                    continue 

                if pas%20==0 and defer%20==0 and fail%20==0: 
                    if pas>=0 and pas<=120 and fail>=0 and fail<=120 :
                        if (pas+defer+fail)!=120: 
                            print("Incorrect total")
                        elif(pas>100 and pas<=120): 
                            print("Progress")
                        elif(pas==100):
                            print("Progress (module trailer)")
                        elif(pas<100 and fail>=0 and fail<80):
                            print("Do not Progress – module retriever")
                        else:
                            print("Exclude")

                    else:
                        print("Out of Range")
                else:
                    print("Out of range")
            except ValueError:
                print("Integer required")
            print("Would you like to enter another set of data ?")
            option=str(input("Enter 'y' for yes or 'n' to quit and view results :"))

        if option=="n" or option=="N":
            print("Thank you for displaying your results")
        
    #THE STAFF VERSION
    elif module_opt==2:
        print("Staff Version with Histogram")
        print()
        option="Y"
        while option=="y" or option=="Y":
            try:
                pas=int(input("Please enter your credits at pass: "))
                if not 0<=pas<=120 or pas%20!=0:
                    print("Out of range")
                    continue
                defer=int(input("Please enter your credit at defer: "))
                if not 0<=defer<=120 or defer%20!=0:
                    print("Out of range")
                    continue
                fail=int(input("Please enter your credit at fail: "))
                if not 0<=fail<=120 or fail%20!=0:
                    print("Out of range")
                    continue

                if pas%20==0 and defer%20==0 and fail%20==0:
                    if pas>=0 and pas<=120 and fail>=0 and fail<=120 :
                        if (pas+defer+fail)!=120:
                            print("Incorrect total")
                        elif(pas>100 and pas<=120):
                            progress_tuple=(pas,defer,fail)
                            progress_list.append(progress_tuple)
                            print("Progress")
                            pro_count+=1
                        elif(pas==100):
                            trailer_tuple=(pas,defer,fail)
                            trailer_list.append(trailer_tuple)
                            print("Progress (module trailer)")
                            pro_m_t_count+=1
                        elif(pas<100 and fail>=0 and fail<80):
                            retriver_tuple=(pas,defer,fail)
                            retriver_list.append(retriver_tuple)
                            print("Do not Progress – module retriever")
                            no_progress+=1
                        else:
                            print("Exclude")
                            exclude_tuple=(pas,defer,fail)
                            exclude_list.append(exclude_tuple)
                            exclude_count+=1
                    else:
                        print("Out of Range")
                else:
                    print("Out of range")
                print()
                print("Would you like to enter another set of data ?")
                option=str(input("Enter 'y' for yes or 'q' to quit and view results :"))

            except ValueError:
                print("Integer required")
        
    

    else:
        print("Pls enter the correct option")
        
    
#calling the function for the main_version
main_version()

#Displaying the results
if option=="q" or option=="Q":
    print("Enter 1------>Horizontal histogram \nEnter 2------>Vertical histogram \nEnter 3------>Progression_list \nEnter 4------>Text_File")
    print()
    menu_opt=int(input("Enter the number between 1 to 4 : "))
    
    if menu_opt==1:
        h_histo()
        
    elif menu_opt==2:
        v_histo()

    elif menu_opt==3:
        progression_list()

    elif menu_opt==4:
        text_file()

    else:
        print("Invaild option")
            

      


              

          
   
    


    

    
    
  
      
    
    





    

