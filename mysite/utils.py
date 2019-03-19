import random
import string


def random_string_generator(size=10, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_patient_id_generator(instance):
    patient_new_id = random_string_generator()

    model_instance = instance.__class__

    qs_exists= model_instance.objects.filter(patientuniqueid=patient_new_id).exists()
    if qs_exists:
        return unique_patient_id_generator(instance)
    return patient_new_id
