from django.db import models

# Create your models here.

class PatientDetails(models.Model):
    patient_id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=50)
    patient_surname = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    phone_number = models.IntegerField
    
    def __str__(self):
        return f"Patient Details {self.patient_name} {self.patient_surname} at {self.phone_number}"
    
    
class Doctors(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    doctor_name = models.CharField(max_length=50)
    doctor_surname = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)
    image = models.ImageField(upload_to='image/Doctors/')

    
    def __str__(self):
        return f"Doctor {self.doctor_name} {self.doctor_surname}"
    
    
class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.department_name   
    
class Appointments (models.Model):
    appointments_id = models.AutoField(primary_key=True)
    patient_name = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    doctor_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    appointment_date = models.DateField
    
    def __str__(self):
        return f"Appointment {self.patient_name} {self.doctor_name} {self.department_name} {self.appointment_date}"