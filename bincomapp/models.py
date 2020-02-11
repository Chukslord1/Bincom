from django.db import models

# Create your models here.
class polling_unit(models.Model):
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()
    uniqueid =  models.IntegerField(primary_key=True)
    polling_unit_id = models.IntegerField()
    uniquewardid = models.IntegerField(null=True)
    polling_unit_number = models.CharField(max_length=12, null=True)
    polling_unit_name = models.CharField(max_length=12, null=True)
    polling_unit_description = models.TextField(max_length=100, null= True)
    lat =  models.CharField(max_length=250, null=True)
    long  =  models.CharField(max_length=250, null=True)
    entered_by_user = models.CharField(max_length= 50)
    date_entered = models.CharField(max_length= 8, null=True)
    user_ip_address = models.CharField(max_length= 50)

class ward(models.Model):
    result_id = models.IntegerField(primary_key=True)
    lga_id = models.IntegerField()
    state_id = models.IntegerField(default=25)
    uniqueid =  models.IntegerField()
    party_abbreviation =  models.CharField(max_length=12)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length= 50)
    date_entered = models.CharField(max_length= 8, null=True)
    user_ip_address = models.CharField(max_length= 50)

class states(models.Model):
    state_id = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=50)

class party(models.Model):
    id= models.IntegerField(primary_key=True)
    partyid=  models.CharField(max_length= 11)
    partyname=  models.CharField(max_length= 11)

class lga(models.Model):
    uniqueid =  models.IntegerField(primary_key=True)
    lga_id = models.IntegerField()
    lga_name = models.CharField(max_length=50)
    state_id = models.IntegerField(default=25)
    lga_description = models.TextField()
    entered_by_user = models.CharField(max_length= 50)
    date_entered = models.CharField(max_length= 8, null=True)
    user_ip_address = models.CharField(max_length= 50)

class announced_ward_results(models.Model):
    result_id = models.IntegerField(primary_key=True)
    ward_name = models.CharField(max_length=50)
    party_abbreviation =models.CharField(max_length=4)
    party_score  = models.IntegerField()
    entered_by_user = models.CharField(max_length= 50)
    date_entered = models.CharField(max_length= 8, null=True)
    user_ip_address = models.CharField(max_length= 50)

class announced_state_results(models.Model):
    result_id = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=50)
    party_abbreviation =models.CharField(max_length=4)
    party_score  = models.IntegerField()
    entered_by_user = models.CharField(max_length= 50)
    date_entered = models.CharField(max_length= 8, null=True)
    user_ip_address = models.CharField(max_length= 50)

class announced_pu_results(models.Model):
    result_id = models.IntegerField(primary_key=True)
    polling_unit_uniqueid = models.IntegerField()
    party_abbreviation =  models.CharField(max_length=12)
    party_score  = models.IntegerField()
    entered_by_user = models.CharField(max_length= 50)
    date_entered = models.CharField(max_length= 8, null=True)
    user_ip_address = models.CharField(max_length= 50)

class announced_lga_results(models.Model):
    result_id = models.IntegerField(primary_key=True)
    lga_name = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=12)
    party_score  = models.IntegerField()
    entered_by_user = models.CharField(max_length= 50)
    date_entered = models.CharField(max_length= 8, null=True)
    user_ip_address = models.CharField(max_length= 50)

class agentname(models.Model):
    name_id = models.TextField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255,null=True)
    phone = models.CharField(max_length=13)
    pollingunit_uniqueid = models.IntegerField()

class total_score(models.Model):
    overall_score = models.CharField(max_length=50)
    score = models.IntegerField()
