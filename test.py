from py2neo import Graph,Node,Relationship
import os
# import requests
import datetime

#Use your NEO4J database password
graph = Graph('bolt://silver-cathryn-island-ruth.graphstory.cloud:7687', auth=('silver_cathryn_island_ruth','IGyKoMerrcjVwN4CeJxJ8uqLjo7Me'))


'''
Data format to make graph database with required labels and properties
'''

username = ''
person_id = 1
first_name = "Luis"
middle_name = ""
last_name = "Suarez"
gender = 'male'
technical_skill = ["Java","Grails","Azure"]
non_technical_skill = ["Leadership","Management"]

# work = {
#       'id': 1,
#       'user': 1,
#       'job_title': 'Django Programmer',
#       'organization': 'Infodev Pvt. Ltd.',
#       'location': 'Kathmandu',
#       'responsibilities': 'To develop django programs',
#       'from_date': datetime.date(2019, 1, 1),
#       'to_date': None,
#       'currently_working': False
#       }

company = {

            "companies":
            [
                 {
                    'id': 1,
                    'user': 1,
                    'job_title': 'Django Programmer',
                    'organization': 'Infodev Pvt. Ltd.',
                    'location': 'Kathmandu',
                    'responsibilities': 'To develop django programs',
                    'from_date': datetime.date(2019, 1, 1),
                    'to_date': None,
                    'currently_working': False
                  },
                  {
                    'id': 2,
                    'user': 1,
                    'job_title': 'AI Programmer',
                    'organization': 'Google Pvt. Ltd.',
                    'location': 'California',
                    'responsibilities': 'To develop ML applications',
                    'from_date': datetime.date(2019, 6, 23),
                    'to_date': None,
                    'currently_working': True
                  }
                 
            ]
}


education = {

            "institutes":
            [
                  {
                        'id': 1,
                        'user': 1,
                        'program': 'Computer Engineering',
                        'institution': 'Harvard University',
                        'location': 'Harvard',
                        'degree': 'Masters',
                        'start': datetime.date(2019,1,1),
                        'end': None
                  },
                  {
                        'id': 2,
                        'user': 1,
                        'program': '+2',
                        'institution': 'Harvard High School',
                        'location': 'Harvard',
                        'degree': 'High School',
                        'start': datetime.date(2015,3,1),
                        'end': None
                  }
            ]
}



# '''
#  Create a unique contrain on user with unique user id
#  '''
# graph.run('''CREATE CONSTRAINT ON (p:Person)
# ASSERT p.person_id IS UNIQUE
# ''')



# '''Create a node person with properties
#     id,firstname,lastname,middlename,gender
# '''
# person = Node("Person")
# person['person_id'] = person_id
# person['first_name'] = first_name
# person['middle_name'] = middle_name
# person['last_name'] = last_name
# person['gender'] = gender
# graph.merge(person,"Person",'person_id')


# '''
#     Create node technical skills
#     which tracks all the technical skllis possessed by user'''
# tech_skills = Node("TechnicalSkills")
# tech_skills['type'] = "Technical"
# graph.merge(tech_skills,"TechnicalSkills","type")


# for i in technical_skill:
#     t_skills = Node("Technical")
#     t_skills['skills'] = i
#     graph.merge(t_skills,'Technical','skills')
#     user_technical_skills = Relationship(person, "HAS_SKILL", t_skills)
#     graph.merge(user_technical_skills)
#     technical_skills = Relationship(t_skills, "IS", tech_skills)
#     graph.merge(technical_skills)


# non_tech_skills = Node("NonTechnicalSkills")
# non_tech_skills['name'] = "NonTechnical"
# graph.merge(non_tech_skills,"NonTechnicalSkills","name")


# for i in non_technical_skill:
#     n_skills = Node('NonTechnical')
#     n_skills['skills'] = i
#     graph.merge(n_skills,"NonTechnical",'skills')
#     user_non_technical_skills = Relationship(person,"HAS_SKILL",n_skills)
#     graph.merge(user_non_technical_skills)
#     non_technical_skills = Relationship(n_skills, "IS", non_tech_skills)
#     graph.merge(non_technical_skills)


# '''
#  Create a unique contrain on user work with unique work id
#  '''

# graph.run('''CREATE CONSTRAINT ON (w:Work)
# ASSERT w.work_id IS UNIQUE
# ''')
# for i in company['companies']:
#     work_details = Node('Work')
#     work_details['work_id']= i['id']
#     work_details['job_title']= i['job_title']
#     work_details['organization'] = i['organization']
#     work_details['responsibilities'] = i['responsibilities']
#     work_details['from_date'] = i['from_date']
#     work_details['to_date'] = i['to_date']
#     work_details['currently_working'] = i['currently_working']
#     graph.merge(work_details,"Work","work_id")
#     work_address = Node('CompanyLocation')
#     work_address['company_location'] = i['location']
#     graph.merge(work_address,"CompanyLocation",'company_location')
#     user_work = Relationship(person, "WORKED_IN", work_details)
#     work_place = Relationship(work_details, "IS_IN", work_address)
#     graph.create(user_work)
#     graph.create(work_place)


# graph.run('''CREATE CONSTRAINT ON (i:Institute)
# ASSERT i.education_id IS UNIQUE
# ''')
# for i in education['institutes']:
#     college = Node('Institute')
#     college['education_id'] = i['id']
#     college['institution'] = i['institution']
#     college['degree'] = i['degree']
#     college['program'] = i['program']
#     college['start'] = i['start']
#     college['end'] = i['end']
#     graph.merge(college,"Institute","education_id")
#     college_location = Node('InstituteLocation')
#     college_location['institute_location'] = i['location']
#     graph.merge(college_location,"InstituteLocation",'institute_location')
#     user_education = Relationship(person, "WENT_TO", college)
#     college_place = Relationship(college, "IS_IN", college_location)
#     graph.create(user_education)
#     graph.create(college_place)

# # Make the unique job according to id
# '''
# # Create a unique contrain on job with unique job id
# # '''
# graph.run('''CREATE CONSTRAINT ON (j:Job)
# ASSERT j.job_id IS UNIQUE
# ''')


# job_id = 4
# job_title = 'BI Analyst'
# deadline = datetime.date(2019,5,15)
# now= datetime.date.today()
# days_remaining = ((deadline - now).days)
# job_technical_skill = ["CC","HR","CFO","Manager","Executive"]
# job_non_skill = ['Communication','Scheduling','Event Handling',"leadership"]


# #Create the job with properties
# job = Node("Job")
# job['job_id'] = job_id
# job['job_title'] = job_title
# job['deadline'] = deadline
# job['days_remaining'] = days_remaining
# graph.merge(job,"Job",'job_title')


# for j in job_technical_skill:
#     t_skills = Node("Technical")
#     t_skills['skills'] = j
#     graph.merge(t_skills,'Technical','skills')
#     job_technical_skills = Relationship(job, "REQUIRED_T_SKILL", t_skills)
#     graph.merge(job_technical_skills)
#     technical_skills = Relationship(t_skills, "IS", tech_skills)
#     graph.merge(technical_skills)

# for j in job_non_skill:
#     n_skills = Node('NonTechnical')
#     n_skills['skills'] = j
#     graph.merge(n_skills,"NonTechnical",'skills')
#     job_non_technical_skills = Relationship(job,"REQUIRED_N_SKILL",n_skills)
#     graph.merge(job_non_technical_skills)
#     non_technical_skills = Relationship(n_skills, "IS", non_tech_skills)
#     graph.merge(non_technical_skills)



# #If anyone applies for any job
# applied = True
# applied_id = 3  #application id
# person_applied = 5  #id of the person who applied for the job 
# applied_job = 4  #id of the job which the person applied

# if applied == True:
#     results = graph.run('''MATCH (p:Person{person_id:{person_applied}}), (j:Job{job_id:{applied_job}})
#                             MERGE (p)-[:APPLIED_FOR]->(j)
#                             RETURN p,j
#                         ''',person_applied = person_applied, applied_job = applied_job )
#     # records = list(results)



# #Query for recommendation
# recommended_results = graph.run('''
# 		MATCH (p:Person) WHERE p.first_name CONTAINS 'Theon'
#         MATCH (j:Job)
#         WHERE j.days_remaining > 0
# 		MATCH (p)-[:HAS_SKILL]->(t_skills)<-[:REQUIRED_T_SKILL]-(j) 
# 		WHERE NOT EXISTS ((p)-[:APPLIED_FOR]->(j)) 
#         RETURN j.job_title,j.days_remaining,
# 			COUNT(*) AS skillsInCommon,
# 			COLLECT(t_skills.skills) AS skills
# 		ORDER BY skillsInCommon DESC
# 		LIMIT 10
# 		''')
# recommended_records = list(recommended_results)

# for row in recommended_records:
#     key = row.keys()
#     value = row.values()
#     print(key)
#     print(value)

# Update the node person
def update_person(person_id,first_name,middle_name,last_name,gender):
    graph.run('''MERGE (p:Person{person_id: {person_id}})
                 SET p = {person_id:{person_id},first_name:{first_name},last_name:{last_name},middle_name:{middle_name},gender:{gender}}
                 RETURN p
        ''', person_id=person_id,first_name=first_name,last_name=last_name,middle_name=middle_name,gender=gender)

# update_person(person_id,first_name,middle_name,last_name,gender)

#Update user technical skills
def update_user_technical_skill(person_id,technical_skill):
    graph.run('''MATCH (p:Person{person_id:{person_id}})-[r:HAS_SKILL]->(t:Technical)
                 DELETE r
                ''',person_id=person_id)
    for i in technical_skill:
        t_skills = Node("Technical")
        t_skills['skills'] = i
        graph.merge(t_skills,'Technical','skills')
        graph.run('''MATCH (p:Person{person_id:{person_id}}),(t:Technical{skills:{i}}) MERGE (p)-[:HAS_SKILL]->(t) 
              ''',person_id=person_id,i=i)
        graph.run(''' MATCH (ts:Technical{skills:{i}}),(tss:TechnicalSkills) MERGE (ts)-[:IS]->(tss)
              ''',i=i)
# update_user_technical_skill(person_id,technical_skill)

#Update user technical skills
def update_user_non_technical_skill(person_id,non_technical_skill):
    graph.run('''MATCH (p:Person{person_id:{person_id}})-[r:HAS_SKILL]->(nt:NonTechnical)
                 DELETE r
                ''',person_id=person_id)
    for i in non_technical_skill:
        n_skills = Node("NonTechnical")
        n_skills['skills'] = i
        graph.merge(n_skills,'NonTechnical','skills')
        graph.run('''MATCH (p:Person{person_id:{person_id}}),(n:NonTechnical{skills:{i}}) MERGE (p)-[:HAS_SKILL]->(n) 
              ''',person_id=person_id,i=i)
        graph.run(''' MATCH (nts:NonTechnical{skills:{i}}),(ntss:NonTechnicalSkills) MERGE (nts)-[:IS]->(ntss)
              ''',i=i)
# update_user_non_technical_skill(person_id,non_technical_skill)
#  for i in company['companies']:
#             company_location'] = i['location']
work = {
      'id': 1,
      'user': 1,
      'job_title': 'Database Developer',
      'organization': 'Infodev Pvt. Ltd.',
      'location': 'Sanepa',
      'responsibilities': 'To develop database architecture',
      'from_date': datetime.date(2019, 3, 1),
      'to_date': None,
      'currently_working': True
      }
print("YE",work['id'])

def update_user_work(person_id,work):
      work_id = work['id']
      title = work['job_title']
      organization = work['organization']
      company_location = work['location']
      responsibility = work['responsibilities']
      from_date = work['from_date']
      to_date = work['to_date']
      currently_working = work['currently_working']


      graph.run('''MATCH (w:Work{work_id: {work_id}})
                   SET w = {work_id:{work_id},job_title:{title},organization:{organization},responsibilities:{responsibility},from_date:{from_date},to_date:{to_date},currenty_working:{currently_working}}
                   RETURN w
                ''', work_id=work_id,title=title,organization=organization,responsibility=responsibility,from_date=from_date,to_date=to_date,currently_working=currently_working)
      graph.run('''MATCH (w:Work{work_id:{work_id}}),(l:CompanyLocation) MERGE (w)-[r:IS_IN]->(l)
                   DELETE r
                ''',work_id=work_id)
      graph.run('''MERGE (cl:CompanyLocation {company_location:{company_location}})
                ''',company_location=company_location)
      graph.run('''MATCH (wk:Work{work_id:{work_id}}),(clo:CompanyLocation {company_location:{company_location}}) MERGE (wk)-[r:IS_IN]->(clo)
                  RETURN clo
            ''',work_id=work_id,company_location=company_location)
      
update_user_work(person_id,work)

edu = {
      'id': 1,
      'user': 1,
      'program': 'Civil Engineering',
      'institution': 'Kathmandu University',
      'location': 'Kathmandu',
      'degree': 'Bachelor',
      'start': datetime.date(2019,3,1),
      'end': None
      }

def update_user_education(person_id,edu):
      education_id = edu['id']
      program = edu['program']
      institution = edu['institution']
      institute_location = edu['location']
      degree = edu['degree']
      start = edu['start']
      end = edu['end']
      
      
      graph.run('''MATCH (i:Institute{education_id: {education_id}})
                   SET i = {education_id:{education_id},program:{program},degree:{degree},institution:{institution},start:{start},end:{end}}
                   RETURN i
                ''', education_id=education_id,program=program,institution=institution,degree=degree,start=start,end=end)
      graph.run('''MATCH (i:Institute{education_id:{education_id}}),(il:InstituteLocation) MERGE (i)-[r:IS_IN]->(il)
                   DELETE r
                ''',education_id=education_id)
      graph.run('''MERGE (il:InstituteLocation {institute_location:{institute_location}})
                ''',institute_location=institute_location)
      graph.run('''MATCH (i:Institute{education_id:{education_id}}),(il:InstituteLocation {institute_location:{institute_location}}) MERGE (i)-[r:IS_IN]->(il)
                  RETURN il
            ''',education_id=education_id,institute_location=institute_location)
      
     
update_user_education(person_id,edu)

# def update_user_education(person_id,education):
#     graph.run('''MATCH (p:Person{person_id:{person_id}})-[r:WENT_TO]->(i:Institute)
#                  DELETE r
#                 ''',person_id=person_id)
#     for i in education['institutes']:
#         college = Node('Institute')
#         college['name'] = i['name']
#         name = i['name']
#         college['degree'] = i['degree']
#         # college['program'] = i['program']
#         graph.merge(college,"Institute","name")
#         college_location = Node('InstituteLocation')
#         college_location['institute_location'] = i['location']
#         location = i['location']
#         graph.merge(college_location,"InstituteLocation",'institute_location')
#         # graph.merge(work_address,"CompanyLocation",'company_location')
#         graph.run('''MATCH (p:Person{person_id:{person_id}}),(c:Institute{name:{name}}) MERGE (p)-[:WENT_TO]->(c) 
#               ''',person_id=person_id,name=name)
#         graph.run('''MATCH (in:Institute{name:{name}})-[r:IS_IN]->(il:InstituteLocation)
#                  DELETE r
#                 ''',name=name)
#         graph.run('''MATCH (ins:Institute{name:{name}}),(insl:InstituteLocation{institute_location:{location}}) MERGE (ins)-[:IS_IN]->(insl) 
#               ''',name=name,location=location)
# # update_user_education(person_id,education)


# Update the node job
def update_job(job_id,job_title,deadline,days_remaining):
    graph.run('''MERGE (j:Job{job_id: {job_id}})
                 SET j = {job_id:{job_id},job_title:{job_title},deadline:{deadline},days_remaining:{days_remaining}}
                 RETURN j
        ''', job_id=job_id,job_title=job_title,deadline=deadline,days_remaining=days_remaining)

# update_job(job_id,job_title,deadline,days_remaining)

#Update job technical skills
def update_job_technical_skill(job_id,job_technical_skill):
    graph.run('''MATCH (j:Job{job_id:{job_id}})-[r:REQUIRED_T_SKILL]->(t:Technical)
                 DELETE r
                ''',job_id=job_id)
    for j in job_technical_skill:
        t_skills = Node("Technical")
        t_skills['skills'] = j
        graph.merge(t_skills,'Technical','skills')
        graph.run('''MATCH (j:Job{job_id:{job_id}}),(t:Technical{skills:{j}}) MERGE (j)-[:REQUIRED_T_SKILL]->(t) 
              ''',job_id=job_id,j=j)
        graph.run(''' MATCH (ts:Technical{skills:{j}}),(tss:TechnicalSkills) MERGE (ts)-[:IS]->(tss)
              ''',j=j)
# update_job_technical_skill(job_id,job_technical_skill)

#Update job non technical skills
def update_job_non_technical_skill(job_id,job_non_skill):
    graph.run('''MATCH (j:Job{job_id:{job_id}})-[r:REQUIRED_N_SKILL]->(nt:NonTechnical)
                 DELETE r
                ''',job_id=job_id)
    for j in job_non_skill:
        n_skills = Node("NonTechnical")
        n_skills['skills'] = j
        graph.merge(n_skills,'NonTechnical','skills')
        graph.run('''MATCH (j:Job{job_id:{job_id}}),(nt:NonTechnical{skills:{j}}) MERGE (j)-[:REQUIRED_N_SKILL]->(nt) 
              ''',job_id=job_id,j=j)
        graph.run(''' MATCH (nts:NonTechnical{skills:{j}}),(ntss:NonTechnicalSkills) MERGE (nts)-[:IS]->(ntss)
              ''',j=j)
# update_job_non_technical_skill(job_id,job_non_skill)

#Remove applied status
def remove_applied_status(person_id,job_id):
      graph.run('''MATCH (p:Person{person_id:{person_id}})-[r:APPLIED_FOR]->(j:Job{job_id:{job_id}})
                   DELETE r
                   ''',person_id=person_id,job_id=job_id)
      

# remove_applied_status(person_id,job_id)