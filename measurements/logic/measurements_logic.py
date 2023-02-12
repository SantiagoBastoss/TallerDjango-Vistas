from ..models import Measurement
from variables.logic import variables_logic

def getMeasurements():
    measurements = Measurement.objects.all()
    return measurements


def getMeasurement(mea_pk):
    measurement = Measurement.objects.get(pk=mea_pk)
    return measurement


def createMeasurement(mea):
    measurement = Measurement(variable=variables_logic.get_variable(mea["variable"]),
                              value=mea["value"], unit=mea["unit"], place=mea["place"])
    measurement.save()
    return measurement


def updateMeasurement(mea_pk, new_mea):
    measurement = getMeasurement(mea_pk)
    measurement.variable = variables_logic.get_variable(new_mea["variable"])
    measurement.value = new_mea["value"]
    measurement.unit = new_mea["unit"]
    measurement.place = new_mea["place"]
    measurement.save()
    return measurement


def deleteMeasurement(mea_pk):
    measurement = getMeasurement(mea_pk)
    measurement.delete()
