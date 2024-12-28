count=0
print("Qualification","-->","B.Tech")
num=int(input("enter the number"))
##Male candidate
if(num==1):
    print("MALE")
    NCC=int(input("enter the Grade for NCC      "))
    print("Grade for NCC is:",   NCC)
##Semester1
    Eng=int(input("enter the english marks"))
    Phy=int(input("enter the physics marks"))
    M1=int(input("enter the maths marks"))
    Draw=int(input("enter the ed marks"))
    C=int(input("enter the c language marks"))
    if((Eng>=35) and (Phy>=35) and (M1>=35) and (Draw>=35) and (C>=35)):
        print("pass")
        total=Eng+Phy+M1+Draw+C
        avg0=total/5
        print(total)
        print(avg0)
        per=total*100/500
        print(per)
        print("the sem1 aggregation is:",per)
    else:
        count+=1
        per=0
        print("the backlog count is :",count)
##Semester2
    M2=int(input("enter the maths marks"))
    Che=int(input("enter the chemistry marks"))
    NA=int(input("enter the Network analysis marks"))
    java=int(input("enter the java marks"))
    Bee=int(input("enter the electronics marks"))
    if((M2>=35) and (Che>=35) and (NA>=35) and (java>=35) and (Bee>=35)):
        print("pass")
        total1=M2+Che+NA+java+Bee
        avg1=total1/5
        print(total1)
        print(avg1)
        per1=total1*100/500
        print(per1)
        print("the sem2 aggregation is:",per1)
    else:
        count+=1
        per1=0
    print("the backlog count is :",count)
##Semester3
    M3=int(input("enter the maths marks"))
    Python=int(input("enter the Phyton marks"))
    Rvsp=int(input("enter the RVSP marks"))
    Lcs=int(input("enter the LCS marks"))
    Stld=int(input("enter the electronics marks"))
    if((M3>=35) and (Python>=35) and (Rvsp>=35) and (Stld>=35) and (Lcs>=35)):
        print("pass")
        total2=M3+Python+Rvsp+Lcs+Stld
        avg2=total2/5
        print(total2)
        print(avg2)
        per2=total2*100/500
        print(per2)
        print("the sem3 aggregation is:",per2)
    else:
        count+=1
        per2=0
    print("the backlog count is:",count)
##Semester4
    Dicd=int(input("enter the Dicd marks"))
    SS=int(input("enter the signals and systems marks"))
    Edc=int(input("enter the EDC marks"))
    Eca=int(input("enter the ECA marks"))
    sub=int(input("enter the sub marks"))
    if((Dicd>=35) and (SS>=35) and (Edc>=35) and (Eca>=35) and (sub>=35)):
        print("pass")
        total3=Dicd+SS+Edc+Eca+sub
        avg3=total3/5
        print(total3)
        print(avg3)
        per3=total3*100/500
        print(per3)
        print("the sem4 aggregation is:",per3)
    else:
        count+=1
        per3=0
    print("the backlog count is :",count)
##Semester5
    Cao=int(input("enter the cao marks"))
    Dsp=int(input("enter the DSP marks"))
    Aica=int(input("enter the AICA marks"))
    Emtl=int(input("enter the EMTL marks"))
    sub2=int(input("enter the sub2 marks"))
    if((Cao>=35) and (Dsp>=35) and (Aica>=35) and (Emtl>=35) and (sub2>=35)):
        print("pass")
        total4=Cao+Dsp+Aica+Emtl+sub2
        avg4=total4/5
        print(total4)
        print(avg4)
        per4=total4*100/500
        print(per4)
        print("the sem5 aggregation is:",per4)
    else:
        count+=1
        per4=0
    print("the backlog count is :",count)
##Semester6
    Sub3=int(input("enter the cao marks"))
    Mpmc=int(input("enter the MPMC marks"))
    Dbms=int(input("enter the DBMS marks"))
    sub4=int(input("enter the sub4 marks"))
    sub5=int(input("enter the sub5 marks"))
    if((Sub3>=35) and (Mpmc>=35) and (Dbms>=35) and (sub4>=35) and (sub5>=35)):
        print("pass")
        total5=Sub3+sub4+Dbms+Mpmc+sub5
        avg5=total5/5
        print(total5)
        print(avg5)
        per5=total5*100/500
        print(per5)
        print("the sem6 aggregation is:",per5)
    else:
        count+=1
        per5=0
    print("the backlog count is :",count)
##Semester7
    Cmos=int(input("enter the dicd cmos marks"))
    Iot=int(input("enter the IOT marks"))
    Cns=int(input("enter the CNS marks"))
    Dip=int(input("enter the DIP marks"))
    Hss=int(input("enter the sub2 marks"))
    if((Cmos>=35) and (Dip>=35) and (Iot>=35) and (Cns>=35) and (Hss>=35)):
        print("pass")
        total6=Cmos+Dip+Iot+Cns+Hss
        avg6=total6/5
        print(total6)
        print(avg6)
        per6=total6*100/500
        print(per6)
        print("the sem7 aggregation is:",per6)
    else:
        count+=1
        per6=0
    print("the backlog count is :",count)
##Semester8
    project=int(input("enter the marks secured in project:"))
    if(project>=100):
        print("pass")
        per7=project*100/500
        print("the project aggregation is ",per7) 
    else:
        print("fail")
        count+=1
        per7=0
    print("the backlog count is:",count)
    if((per!=0) and (per2!=0) and (per3!=0) and (per4!=0) and (per5!=0) and (per6!=0) and (per7!=0)):
        points=per+per1+per2+per3+per4+per5+per6+per7
        print("the total points is:",points)
        average=points/8
        print("The average aggregate for semesters is:", average)
        percentage=points*100/800  
        print("The percentage is",percentage)
    ##if pass then selected for written test##
        if(percentage>=75 and NCC>=95 and count<=2):
            print("Candidate is qualified for written test")
            print("Written Test:"   ,   "Total Marks : 200")
            print("Core"    ,   "Marks : 150")
            print("verbal"  ,   "Marks : 10")
            print("Apptitude"   ,   "Marks : 25")
            print("Reasoning"   ,   "Marks : 15")
        Core=int(input("enter the marks secured in core"))
        Verbal=int(input("enter the marks secured in verbal"))
        Apptitude=int(input("enter the marks secured in Apptitude"))
        Reasoning=int(input("enter the marks secured in Reasoning"))
        if((Core>=70) and (Verbal>=5) and (Apptitude>=15) and (Reasoning>=7)):
            avgw=Core+Verbal+Apptitude+Reasoning/4
        print("the marks secured in the test is:",avgw)
        print("The candidate is eligible for personal interview")
        print("Personal Interview:")
        print("Tell me about yourself")
        print(" I am so n so **********************************")
        print("you can submit your certificates")
        print("Bond:")
        print("Signature on the bond that you are going to work under the company alliances for 5 years")
        sign=input("singnature")
        print(sign)
        print("OFFER LETTER")
        print("THANK YOU")
    else:
        print("Will get back to you")
        print("Thank you")
print("EXIT")
##Female cadidate
if(num==2):
    print("FEMALE")
    NCC=int(input("enter the Grade for NCC      "))
    print("Grade for NCC is:",   NCC)
##Semester1
    Eng=int(input("enter the english marks"))
    Phy=int(input("enter the physics marks"))
    M1=int(input("enter the maths marks"))
    Draw=int(input("enter the ed marks"))
    C=int(input("enter the c language marks"))
    if((Eng>=35) and (Phy>=35) and (M1>=35) and (Draw>=35) and (C>=35)):
        print("pass")
        total=Eng+Phy+M1+Draw+C
        avg0=total/5
        print(total)
        print(avg0)
        per=total*100/500
        print(per)
        print("the sem1 aggregation is:",per)
    else:
        count+=1
        per=0
        print("the backlog count is :",count)
##Semester2
    M2=int(input("enter the maths marks"))
    Che=int(input("enter the chemistry marks"))
    NA=int(input("enter the Network analysis marks"))
    java=int(input("enter the java marks"))
    Bee=int(input("enter the electronics marks"))
    if((M2>=35) and (Che>=35) and (NA>=35) and (java>=35) and (Bee>=35)):
        print("pass")
        total1=M2+Che+NA+java+Bee
        avg1=total1/5
        print(total1)
        print(avg1)
        per1=total1*100/500
        print(per1)
        print("the sem2 aggregation is:",per1)
    else:
        count+=1
        per1=0
    print("the backlog count is :",count)
##Semester3
    M3=int(input("enter the maths marks"))
    Python=int(input("enter the Phyton marks"))
    Rvsp=int(input("enter the RVSP marks"))
    Lcs=int(input("enter the LCS marks"))
    Stld=int(input("enter the electronics marks"))
    if((M3>=35) and (Python>=35) and (Rvsp>=35) and (Stld>=35) and (Lcs>=35)):
        print("pass")
        total2=M3+Python+Rvsp+Lcs+Stld
        avg2=total2/5
        print(total2)
        print(avg2)
        per2=total2*100/500
        print(per2)
        print("the sem3 aggregation is:",per2)
    else:
        count+=1
        per2=0
    print("the backlog count is:",count)
##Semester4
    Dicd=int(input("enter the Dicd marks"))
    SS=int(input("enter the signals and systems marks"))
    Edc=int(input("enter the EDC marks"))
    Eca=int(input("enter the ECA marks"))
    sub=int(input("enter the sub marks"))
    if((Dicd>=35) and (SS>=35) and (Edc>=35) and (Eca>=35) and (sub>=35)):
        print("pass")
        total3=Dicd+SS+Edc+Eca+sub
        avg3=total3/5
        print(total3)
        print(avg3)
        per3=total3*100/500
        print(per3)
        print("the sem4 aggregation is:",per3)
    else:
        count+=1
        per3=0
    print("the backlog count is :",count)
##Semester5
    Cao=int(input("enter the cao marks"))
    Dsp=int(input("enter the DSP marks"))
    Aica=int(input("enter the AICA marks"))
    Emtl=int(input("enter the EMTL marks"))
    sub2=int(input("enter the sub2 marks"))
    if((Cao>=35) and (Dsp>=35) and (Aica>=35) and (Emtl>=35) and (sub2>=35)):
        print("pass")
        total4=Cao+Dsp+Aica+Emtl+sub2
        avg4=total4/5
        print(total4)
        print(avg4)
        per4=total4*100/500
        print(per4)
        print("the sem5 aggregation is:",per4)
    else:
        count+=1
        per4=0
    print("the backlog count is :",count)
##Semester6
    Sub3=int(input("enter the cao marks"))
    Mpmc=int(input("enter the MPMC marks"))
    Dbms=int(input("enter the DBMS marks"))
    sub4=int(input("enter the sub4 marks"))
    sub5=int(input("enter the sub5 marks"))
    if((Sub3>=35) and (Mpmc>=35) and (Dbms>=35) and (sub4>=35) and (sub5>=35)):
        print("pass")
        total5=Sub3+sub4+Dbms+Mpmc+sub5
        avg5=total5/5
        print(total5)
        print(avg5)
        per5=total5*100/500
        print(per5)
        print("the sem6 aggregation is:",per5)
    else:
        count+=1
        per5=0
    print("the backlog count is :",count)
##Semester7
    Cmos=int(input("enter the dicd cmos marks"))
    Iot=int(input("enter the IOT marks"))
    Cns=int(input("enter the CNS marks"))
    Dip=int(input("enter the DIP marks"))
    Hss=int(input("enter the sub2 marks"))
    if((Cmos>=35) and (Dip>=35) and (Iot>=35) and (Cns>=35) and (Hss>=35)):
        print("pass")
        total6=Cmos+Dip+Iot+Cns+Hss
        avg6=total6/5
        print(total6)
        print(avg6)
        per6=total6*100/500
        print(per6)
        print("the sem7 aggregation is:",per6)
    else:
        count+=1
        per6=0
    print("the backlog count is :",count)
##Semester8
    project=int(input("enter the marks secured in project:"))
    if(project>=100):
        print("pass")
        per7=project*100/500
        print("the project aggregation is ",per7) 
    else:
        print("fail")
        count+=1
        per7=0
    print("the backlog count is:",count)
    if((per!=0) and (per2!=0) and (per3!=0) and (per4!=0) and (per5!=0) and (per6!=0) and (per7!=0)):
        points=per+per1+per2+per3+per4+per5+per6+per7
        print("the total points is:",points)
        average=points/8
        print("The average aggregate for semesters is:", average)
        percentage=points*100/800  
        print("The percentage is",percentage)
    ##if pass then selected for written test##
        if(percentage>=75 and NCC>=95 and count<=2):
            print("Candidate is qualified for written test")
            print("Written Test:"   ,   "Total Marks : 200")
            print("Core"    ,   "Marks : 150")
            print("verbal"  ,   "Marks : 10")
            print("Apptitude"   ,   "Marks : 25")
            print("Reasoning"   ,   "Marks : 15")
        Core=int(input("enter the marks secured in core"))
        Verbal=int(input("enter the marks secured in verbal"))
        Apptitude=int(input("enter the marks secured in Apptitude"))
        Reasoning=int(input("enter the marks secured in Reasoning"))
        if((Core>=70) and (Verbal>=5) and (Apptitude>=15) and (Reasoning>=7)):
            avgw=Core+Verbal+Apptitude+Reasoning/4
        print("the marks secured in the test is:",avgw)
        print("The candidate is eligible for personal interview")
        print("Personal Interview:")
        print("Tell me about yourself")
        print(" I am so n so **********************************")
        print("you can submit your certificates")
        print("Bond:")
        print("Signature on the bond that you are going to work under the company alliances for 5 years")
        sign=input("singnature")
        print(sign)
        print("OFFER LETTER")
        print("THANK YOU")
    else:
        print("Will get back to you")
        print("Thank you")
    print("EXIT")
     
        
    

     
        
    
