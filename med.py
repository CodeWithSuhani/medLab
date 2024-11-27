from datetime import datetime 
from datetime import timedelta
import random

class medlabgo:
     def book_a_test():
          name=input()
          #print("for kids(1 upto 11 yrs) press 2")
          #print("for teenagers(11 upto 18 yrs) press 3")
          #print("for adults press 4")
          age_grp=input()#use later to add 'months' or 'years' old and further for tests
          dag={"0 to 1 years":1,"2 to 10 years":2,"11 to 18 years":3,"Above 18":4}
          if age_grp in dag:
               ag=dag[age_grp]
          age=int(input())
          gen=input()
          date=input()#10-11-2005 format
          hadd=input()
          city=input()
          pn=input()
          em=input()
          doc=["Dr.Vipul Verma","Dr.Manoj Sondhi","Dr.Krishna Kumar Tripathi","Dr.Rachnindar Kaur"]
          dp=["+91 8124482169","+91 8128891967","+91 8127083152","+91 8123046122"]
          addr=["3-F, Jaypee nagar","11-7, M.G.Road","G-2,Kailash Nagar","9-C,Khandari road"]
          c=0
          if gen=="female":
               c=1
          elif gen=="male":
               c=2
          elif gen=="other":
               c=3
          #book a visit
          #vaccination
          #tests form
          test=[]
          cat=""
     
          match ag:
                 case 1:
                    if age>=0 and age<=2:#blood tests can be done at home and clinic(reccomended)
                          test=["1.Blood group with Rh factor",
                              "2.Immunoglobulin assessment",
                              "3.Polymerase chain reaction and HIV screening",
                              "4.Liver Function Tests to assess neonatal jaundice"]
                          costs = [145, 1000, 2000, 500]
                          cat="New Born Baby"
                    else:#blood tests clinic recommended
                         test=["1.Hemoglobin abnormalities",
                              "2.Screening for nutritional deficiencies",
                              "3.Anti Hepatitis C virus"]
                         costs = [400, 1150, 850]
                         cat="Infant"
                 case 2:
                    cat="Child"
                    match c:
                         case 2:#scheduling a visit is highly recommended from list index 3 to end
                              test=["1.Complete Blood Count (CBC)",
                               "2.Blood Chemistry Tests",
                               "3.Testosterone Levels",
                               "4.Tuberculosis (TB) Test",
                               "5.Lead Exposure Blood Testing",
                               "6.Stool Tests",
                               "7.Growth and Development Tests",
                               "8.Hearing Screenings",
                               "9.Eye Exams and Vision Screenings",
                               "10.Urinalysis","Lead Exposure Blood Testing",
                               "11.Cholesterol Screenings",
                               "12.Hepatitis C Virus (HCV) Test",
                               "13.Human Immunodeficiency Virus (HIV) Test"]
                              costs = [250, 550, 750, 550, 1150, 350, 2000, 1000, 750, 300, 500, 1000, 750]
                         case 1:#scheduling a visit is highly recommended from list index 3 to end
                              test=["1.Complete Blood Count (CBC)",
                               "2.Blood Chemistry Tests",
                               "3.Follicle-Stimulating Hormone (FSH) and Luteinizing Hormone (LH) Levels",
                               "4.Tuberculosis (TB) Test",
                               "5.Lead Exposure Blood Testing",
                               "6.Stool Tests",
                               "7.Growth and Development Tests",
                               "8.Hearing Screenings",
                               "9.Eye Exams and Vision Screenings",
                               "10.Urinalysis","Lead Exposure Blood Testing",
                               "11.Cholesterol Screenings",
                               "12.Hepatitis C Virus (HCV) Test",
                               "13.Human Immunodeficiency Virus (HIV) Test"]
                              costs = [1450, 800, 750, 1000, 1400, 750, 600, 600, 1500, 650,900,550,1200]
                         case 3:#scheduling a visit is highly recommended from list index 4 and 5
                              test=["1.Complete Blood Count (CBC) to monitor blood cell counts",
                               "2.Electrolyte panel to monitor electrolyte levels",
                               "3.Liver function tests to monitor liver health",
                               "4.Level checks to monitor the effects of hormone therapy",
                               "5.Bone density scan to monitor bone health ",
                               "6.Thyroid function tests to monitor thyroid health"]
                              costs = [2500, 650,550,1450,750,200]
                 case 3:
                    cat="Adolescent"
                    match c:
                         case 1:#scheduling a visit is highly recommended from list index 3
                              test=["1.Complete Blood Count (CBC)",
                               "2.Blood Chemistry Tests",
                               "3.Screening for HIV, HBsAg, syphilis, gonorrhea, and Chlamydia",
                               "4.Radiography - Chest x-ray",
                               "5.Abdominal ultrasound",
                               "6.Gynecological Examination"]
                              costs = [200, 300, 800, 300, 1000, 500]
                         case 2:#scheduling a visit is highly recommended from list index 3
                              test=["1.Complete Blood Count (CBC)",
                               "2.Blood Chemistry Tests",
                               "3.Screening for HIV, HBsAg, syphilis, gonorrhea, and Chlamydia",
                               "4.Radiography  Chest x-ray",
                               "5.Abdominal ultrasound"]
                              costs = [200, 300, 800, 300, 1000]
                         case 3:#scheduling a visit is highly recommended from list index 3
                              test=["1.Blood Chemistry Tests",
                               "2.Complete Blood Count (CBC) to monitor blood cell counts",
                               "3.Electrolyte panel to monitor electrolyte levels",
                               "4.Liver function tests to monitor liver health",
                               "5.Hormone level checks to monitor the effects of hormone therapy",
                               "6.Bone density scan to monitor bone health ",
                               "7.Thyroid function tests to monitor thyroid health"]
                              costs = [300, 200, 400, 500, 600, 1500, 500]
                 case 4:
                    cat="Adult"
                    if age>=18 and age<30:
                         match c:
                              case 1:#clinic visit reccommended after list index 5
                                   test=["1.Blood Pressure, Body Weight, Height, and Body Mass Index: Annually",
                                    "2.Blood Investigations- Complete Blood Count",
                                     "3.Liver function tests",
                                     "4.Renal function tests",
                                      "5.Lipid profile analysis", 
                                      "6.Blood sugar levels - fasting and post-prandial",
                                      "7.Serological tests for HIV, HbsAg, and HCV",
                                      "8.Urine - Routine and Microscopic Examination",
                                      "9.Radiology - Chest x-ray and Abdominal Ultrasound",
                                      "10.Breast Examination - After the age of 20 years",
                                      "11.Visual and Auditory Assessment: Annually",
                                      "12.Oral and Dental Health Assessment: Annually",
                                      "13.Cardiac Health Status Check - ECG and 2D echocardiography",
                                      "14.Gynecological assessment - Pap smear and pelvic examination "]
                                   costs = [650,475,700,750,850,400,850,250,500,1000,1500,850,1000,2300]
                              case 2:#clinic visit reccommended after list index 5
                                   test=["1.Blood Pressure, Body Weight, Height, and Body Mass Index: Annually",
                                    "2.Blood Investigations- Complete Blood Count",
                                     "3.Liver function tests",
                                     "4.1,2,3,4Renal function tests",
                                      "5.Lipid profile analysis", 
                                      "6.Blood sugar levels - fasting and post-prandial",
                                      "7.Serological tests for HIV, HbsAg, and HCV",
                                      "8.Urine - Routine and Microscopic Examination",
                                      "9.Radiology - Chest x-ray and Abdominal Ultrasound",
                                      "10.Visual and Auditory Assessment: Annually",
                                      "11.Oral and Dental Health Assessment: Annually",
                                      "12.Cardiac Health Status Check - ECG and 2D echocardiography"]
                                   costs=[650, 475, 700, 750, 850, 400, 850, 250, 500, 1000, 1500,1200]
                              case 3:#clinic visit recommended after list index 5
                                   test=["1.Complete Blood Count (CBC) to monitor blood cell counts",
                                    "2.Electrolyte panel to monitor electrolyte levels",
                                    "3.Liver function tests to monitor liver health",
                                    "4.Hormone level checks to monitor the effects of hormone therapy",
                                    "5.Lipid profile to monitor cholesterol and triglyceride levels",
                                    "6.Blood glucose testing to monitor blood sugar levels",
                                    "7.Clinic - Pelvic exam",
                                    "8.Clinic - Pap smear",]
                                   costs=[650, 475, 700, 750, 850, 400, 850, 250]
                    elif age>=30 and age<50:
                         match c:
                              case 1:#clinic visit reccommended after list index 1
                                   test=["1.Blood pressure, body weight, and body mass index: Annually",
                                    "2.Complete blood count, Lipid profile, liver function test, renal function test, blood sugar levels",
                                    "3.Serology for HIV, HCV, and HbsAg",
                                    "4.Radiology - Chest X Ray and Abdominal Ultrasound",
                                    "5.Visual, Auditory, and Oral Health Assessment: Annually",
                                    "6.Cardiac Health - ECG and 2D echocardiography",
                                    "7.Bone Health Assessment",
                                    "8.Breast Examination - After the age of 40 years",
                                    "9.Gynecological Examination - Pap smear and pelvic examination"]
                                   costs= [650, 475, 850, 500, 1000, 1500, 2300, 2750, 1750]

                              case 2:#clinic visit reccommended after list index 1
                                   test=["1.Blood pressure, body weight, and body mass index: Annually",
                                    "2.Complete blood count, Lipid profile, liver function test, renal function test, blood sugar levels",
                                    "3.Serology for HIV, HCV, and HbsAg",
                                    "4.Radiology - Chest X Ray and Abdominal Ultrasound",
                                    "5.Visual, Auditory, and Oral Health Assessment: Annually",
                                    "6.Cardiac Health - ECG and 2D echocardiography",
                                    "7.Bone Health Assessment"]
                                   costs=[650, 475, 850, 500, 1000, 1500, 2300]
                              case 3:#clinic visit reccommended after list index 5
                                   test=["1.Complete Blood Count (CBC) to monitor blood cell counts",
                                    "2.Electrolyte panel to monitor electrolyte levels",
                                    "3.Liver function tests to monitor liver health",
                                    "4.Hormone level checks to monitor the effects of hormone therapy",
                                    "5.Lipid profile to monitor cholesterol and triglyceride levels",
                                    "6.Blood glucose testing to monitor blood sugar levels",
                                    "7.Prostate-Specific Antigen (PSA) testing (for non-binary individuals assigned male at birth)",
                                    "8.Mammography or breast MRI (for non-binary individuals assigned female at birth)",
                                    "9.Colonoscopy"]
                                   costs=[475, 750, 700, 1000, 850, 400, 1500, 2000, 2500]
                    else:
                         match c:
                              case 1:#clinic visit recommended after list index 4
                                   test=["1.Blood pressure, Body Weight, and Body Mass Index: Annually",
                                    "2.Complete Blood Count",
                                    "3.Renal function test",
                                    "4.Liver function test",
                                    "5.Blood sugar levels",
                                    "6.Serology for HIV, HCV, and HbsAg",
                                    "7.Colonic Health - per-rectal and colonoscopy examination for females",
                                    "8.Pap smear and pelvic examination for females",
                                    "9.Breast health examination for females - physical examination and mammography",
                                    "10.Bone Health Assessment",
                                    "11.Visual, auditory, and oral health assessment: Annually or as per advise",
                                    "12.Cardiac health check -ECG and 2D echocardiography ",
                                    "13.Respiratory status analysis - chest x-ray and spirometry"]
                                   costs=[650, 475, 750, 700, 400, 850, 2000, 1500, 1000, 2000, 1500, 2300, 1800]
                              case 2:#clinic visit recommended after list index 5
                                   test=["1.Blood pressure, Body Weight, and Body Mass Index: Annually",
                                    "2.Complete Blood Count",
                                    "3.Renal function test",
                                    "4.Liver function test",
                                    "5.Blood sugar levels",
                                    "6.Serology for HIV, HCV, and HbsAg",
                                    "7.Serum Prostate Specific Antigen in males",
                                    "8.Bone Health Assessment",
                                    "9.Visual, auditory, and oral health assessment: Annually or as per advise",
                                    "10.Cardiac health check - ECG and 2D echocardiography ",
                                    "11.Respiratory status analysis - chest x-ray and spirometry"]
                                   costs=[650, 475, 750, 700, 400, 850, 1500, 1000, 1500, 2300, 1800]
                              case 3:#clinic visit recommended after list index 5
                                   test=["1.Complete Blood Count (CBC) to monitor blood cell counts",
                                    "2.Electrolyte panel to monitor electrolyte levels",
                                    "3.Liver function tests to monitor liver health",
                                    "4.Hormone level checks to monitor the effects of hormone therapy",
                                    "5.Lipid profile to monitor cholesterol and triglyceride levels",
                                    "6.Blood glucose testing to monitor blood sugar levels",
                                    "7.Prostate-Specific Antigen (PSA) testing (for non-binary individuals assigned male at birth)",
                                    "8.Mammography or breast MRI (for non-binary individuals assigned female at birth)",
                                    "9Colonoscopy","Clinic - Bone density scan to monitor bone health",
                                    "Thyroid function tests to monitor thyroid health (if applicable)"]
                                   costs=[475, 750, 700, 1000, 850, 400, 1500, 2000, 2500, 2000]
          Dict={}
          Dict["TESTS"]="PRICES"
          for t in test:
               i=test.index(t)
               Dict[t]=costs[i]
          for key, value in Dict.items():
               print(f"{key:<100} {value}")  # Add 20 spaces before the value
          rl=list(map(int,input().split(",")))
          r=random.randint(0,4)
          s=0
          for i in rl:
               s=s+costs[i-1]
          gst=(18/100)*18
          gst=float("%.2f"%gst)
          amt=s+gst

          report=open("{}.txt".format(name),"w")
          report_list=["NAME:{}".format(name),
          "AGE:{}".format(age),
          "GENDER:{}".format(gen),
          "DATE:{}".format(date),
          "HOME ADDRESS:{}".format(hadd),
          "CITY:{}".format(city),
          "Ph.No.:{}".format(pn),
          "E-Mail:{}".format(em),
          "DOCTOR:{}".format(doc[r]),
          "DOCTOR'S Ph.No.:{}".format(dp[r]),
          "DOCTOR'S ADDRESS:{}".format(addr[r]),
          "SUM OF MONEY:{}".format(s),
          "GST:{}".format(gst),
          "AMOUNT TO BE PAID:{}".format(amt)]
          for lines in report_list:
               report.write(lines+"\n")
          report.close()
     book_a_test()
