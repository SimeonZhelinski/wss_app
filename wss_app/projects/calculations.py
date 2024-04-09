import math
from math import sqrt


def common_calculation(building):
    water_supply_norm_for_residence_building = 200
    equivalent_number_of_faucets = {
        'bathroom_sink': 0.5,
        'kitchen_sink': 1,
        'toilet_seat': 0.5,
        'washing_machine': 1,
        'dishwasher': 1.5,
        'shower': 1,
        'bathtub': 1.5
    }

    enf_total_sum = 0
    for field, equivalent in equivalent_number_of_faucets.items():
        value = getattr(building, field, None)
        if value is not None:
            enf_total_sum += value * equivalent

    max_daily_water_quantity = (water_supply_norm_for_residence_building * building.building_residence) / 1000
    average_daily_water_quantity = max_daily_water_quantity / 1.2
    relative_dimensional_water_quantity = max_daily_water_quantity / enf_total_sum
    dimensional_maximum_second_water_quantity = 0.25 * sqrt(enf_total_sum * (
            relative_dimensional_water_quantity ** 0.6)) + 0.012 * enf_total_sum * relative_dimensional_water_quantity

    fire_water = 0
    if hasattr(building, 'underground_parking_spots') and building.underground_parking_spots is not None:
        if building.underground_parking_spots >= 10:
            fire_water = 5

    dimensional_maximum_second_water_quantity += fire_water

    water_speed = 0
    friction_losses = 0
    diameter = ''
    staff_water_message = ''

    if 0 < dimensional_maximum_second_water_quantity <= 0.23:
        dim_range = (0.23 - 0) * 100
        diameter = 'DN20'
        water_speed = ((1.25 - 0.1) / dim_range) * (
                dimensional_maximum_second_water_quantity - 0) * 100 + 0.1
        friction_losses = ((1.516 - 0.006) / dim_range) * (
                dimensional_maximum_second_water_quantity - 0) * 100 + 0.006

    elif 0.24 <= dimensional_maximum_second_water_quantity <= 0.37:
        dim_range = (0.37 - 0.24) * 100
        diameter = 'DN25'
        water_speed = ((1.21 - 0.76) / dim_range) * (
                dimensional_maximum_second_water_quantity - 0.24) * 100 + 0.76
        friction_losses = ((0.989 - 0.467) / dim_range) * (
                dimensional_maximum_second_water_quantity - 0.24) * 100 + 0.467

    elif 0.38 <= dimensional_maximum_second_water_quantity <= 0.65:
        dim_range = (0.65 - 0.38) * 100
        diameter = 'DN32'
        water_speed = ((1.20 - 0.76) / dim_range) * (
                dimensional_maximum_second_water_quantity - 0.38) * 100 + 0.76
        friction_losses = ((0.759 - 0.294) / dim_range) * (
                dimensional_maximum_second_water_quantity - 0.38) * 100 + 0.294

    elif 0.66 <= dimensional_maximum_second_water_quantity <= 0.99:
        dim_range = (0.99 - 0.66) * 100
        diameter = 'DN40'
        water_speed = ((1.19 - 0.76) / dim_range) * (
                dimensional_maximum_second_water_quantity - 0.66) * 100 + 0.76
        friction_losses = ((0.540 - 0.263) / dim_range) * (
                dimensional_maximum_second_water_quantity - 0.66) * 100 + 0.263

    elif 1.00 <= dimensional_maximum_second_water_quantity <= 1.59:
        dim_range = (1.59 - 1.00) * 100
        diameter = 'DN50'
        water_speed = ((1.195 - 0.80) / dim_range) * (
                dimensional_maximum_second_water_quantity - 1.00) * 100 + 0.80
        friction_losses = ((0.426 - 0.187) / dim_range) * (
                dimensional_maximum_second_water_quantity - 1.00) * 100 + 0.187

    elif 1.60 <= dimensional_maximum_second_water_quantity <= 2.39:
        dim_range = (2.39 - 1.60) * 100
        diameter = 'DN63'
        water_speed = ((1.195 - 0.80) / dim_range) * (
                dimensional_maximum_second_water_quantity - 1.60) * 100 + 0.80
        friction_losses = ((0.290 - 0.142) / dim_range) * (
                dimensional_maximum_second_water_quantity - 1.60) * 100 + 0.142

    elif 2.40 <= dimensional_maximum_second_water_quantity <= 5:
        dim_range = (5 - 2.40) * 100
        diameter = 'DN75'
        water_speed = ((1.70 - 0.80) / dim_range) * (
                dimensional_maximum_second_water_quantity - 2.40) * 100 + 0.80
        friction_losses = ((0.469 - 0.126) / dim_range) * (
                dimensional_maximum_second_water_quantity - 2.40) * 100 + 0.126

    elif 5 < dimensional_maximum_second_water_quantity <= 12.00:
        dim_range = (12.00 - 5) * 100
        diameter = 'DN90'
        water_speed = ((2.44 - 0.69) / dim_range) * (
                dimensional_maximum_second_water_quantity - 5) * 100 + 0.69
        friction_losses = ((0.665 - 0.068) / dim_range) * (
                dimensional_maximum_second_water_quantity - 5) * 100 + 0.068

    else:
        diameter = 'N/A'
        water_speed = 'N/A'
        friction_losses = 'N/A'
        staff_water_message = '** Large dimensional data, for more information please contact us'

    domestic_water_only = dimensional_maximum_second_water_quantity - fire_water

    waste_water_quantity = water_supply_norm_for_residence_building * 0.90
    time_to_fill = 20
    tank_volume_liters = building.building_residence * waste_water_quantity * time_to_fill
    tank_volume_cubic_meters = tank_volume_liters / 1000

    water_meter_type = 'Normal'
    if fire_water > 0:
        water_meter_type = 'Combine'

    result = {
        'diameter': diameter,
        'water_speed': water_speed,
        'friction_losses': friction_losses,
        'tank_volume_liters': tank_volume_liters,
        'tank_volume_cubic_meters': tank_volume_cubic_meters,
        'waste_water_quantity': waste_water_quantity,
        'average_daily_water_quantity': average_daily_water_quantity,
        'dimensional_maximum_second_water_quantity': dimensional_maximum_second_water_quantity,
        'max_daily_water_quantity': max_daily_water_quantity,
        'fire_water': fire_water,
        'domestic_water_only': domestic_water_only,
        'water_meter_type': water_meter_type,
    }

    if staff_water_message != '':
        result['staff_water_message'] = staff_water_message

    return result


class ResidenceBuildingWithoutInfrastructureCalculator:
    def __init__(self, building):
        self.building = building

    def calculate(self):
        return common_calculation(self.building)


class ResidenceBuildingWithInfrastructureCalculator:
    def __init__(self, building):
        self.building = building

    def calculate(self):

        waste_water_equivalent = {
            'bathroom_sink': 0.5,
            'kitchen_sink': 0.8,
            'toilet_seat': 2,
            'washing_machine': 0.8,
            'dishwasher': 0.8,
            'shower': 0.8,
            'bathtub': 0.8,
            'floor_siphon': 0.8,
        }

        waste_water_equivalent_total_sum = 0
        for field, equivalent in waste_water_equivalent.items():
            value = getattr(self.building, field, None)
            if value is not None:
                waste_water_equivalent_total_sum += value * equivalent

        domestic_waste_water_quantity = 0.5 * sqrt(waste_water_equivalent_total_sum)

        building_area_ha = self.building.building_area * 0.0001
        property_area_ha = self.building.property_area * 0.0001
        green_area_ha = self.building.green_area * 0.0001

        building_roof_rain_water = building_area_ha * 0.9 * 314
        parking_rain_water = (property_area_ha - building_area_ha - green_area_ha) * 0.9 * 314
        green_area_rain_water = green_area_ha * 0.3 * 314

        sum_rain_water = building_roof_rain_water + parking_rain_water + green_area_rain_water

        overall_waste_water = domestic_waste_water_quantity + sum_rain_water

        pump_needed = 'No'
        staff_sewer_message = ''

        if self.building.floors > 5:
            pump_needed = 'Yes'

        slope = '1 %'

        if 0 < overall_waste_water <= 11:
            waste_water_speed = 1.20
            waste_water_diameter = 'DN 150'

        elif 11 < overall_waste_water < 20:
            waste_water_speed = 1.28
            waste_water_diameter = 'DN 200'

        elif 20 <= overall_waste_water <= 36:
            waste_water_speed = 1.47
            waste_water_diameter = 'DN 250'

        elif 37 <= overall_waste_water <= 58:
            waste_water_speed = 1.65
            waste_water_diameter = 'DN 300'

        else:
            waste_water_speed = 'N/A'
            waste_water_diameter = 'N/A'
            slope = 'N/A'
            staff_sewer_message = '** Large dimensional data, for more information please contact us'

        result = common_calculation(self.building)
        result['pump_needed'] = pump_needed
        result['domestic_waste_water_quantity'] = domestic_waste_water_quantity
        result['sum_rain_water'] = sum_rain_water
        result['overall_waste_water'] = overall_waste_water
        result['slope'] = slope
        result['waste_water_speed'] = waste_water_speed
        result['waste_water_diameter'] = waste_water_diameter

        if staff_sewer_message != '':
            result['staff_sewer_message'] = staff_sewer_message

        return result


def infrastructure_calculation(building):
    plumbing_diameter = building.new_plumbing_diameter
    sewer_diameter = building.new_sewer_diameter
    plumbing_length = building.new_plumbing_length
    sewer_length = building.new_sewer_length
    settlement_inhabitants = building.settlement_inhabitants
    pavement = building.existing_pavement

    fire_hydrants_price = 800

    plumbing_pipe_with_installation_price = {
        'DN90': 20,
        'DN110': 30,
        'DN125': 40,
        'DN160': 64,
        'DN200': 94,
        'DN225': 118,
        'DN250': 146,
        'DN315': 232,
        'DN355': 304,
        'DN400': 360,
    }

    length_between_fire_hydrants = {
        'Bellow 1000 inhabitants': 200,
        'Bellow 100 000 inhabitants': 150,
        'Above 100 000 inhabitants': 100,
    }

    sewer_pipe_with_installation_price = {
        'DN315': 60,
        'DN400': 90,
        'DN500': 150,
        'DN630': 250,
        'DN800': 340,
        'DN1000': 450,
    }

    length_between_manholes = {
        'DN315': 60,
        'DN400': 60,
        'DN500': 80,
        'DN630': 80,
        'DN800': 100,
        'DN1000': 150,
    }

    pavement_restoration_price = {
        'Asphalt': 210,
        'Concrete': 150,
        'Stone paving': 320,
        'Pavers': 280,
        'None': 0
    }

    excavation_embankment_price = 120
    const_for_sewer_excavation = 1.5

    number_of_fire_hydrants = math.ceil(plumbing_length / length_between_fire_hydrants[settlement_inhabitants])

    total_plumbing_price = (plumbing_pipe_with_installation_price[plumbing_diameter] * plumbing_length) + (
            pavement_restoration_price[pavement] * plumbing_length) + (
                                   excavation_embankment_price * plumbing_length) + (
                                   number_of_fire_hydrants * fire_hydrants_price)

    total_sewer_price = (sewer_pipe_with_installation_price[sewer_diameter] * sewer_length) + (
            pavement_restoration_price[pavement] * sewer_length) + (
                                excavation_embankment_price * sewer_length * const_for_sewer_excavation)

    number_of_inspection_manholes = math.ceil(sewer_length / length_between_manholes[sewer_diameter])

    result = {
        "total_plumbing_price": total_plumbing_price,
        "total_sewer_price": total_sewer_price,
        "number_of_inspection_manholes": number_of_inspection_manholes,
        "number_of_fire_hydrants": number_of_fire_hydrants,
    }

    return result


class InfrastructureCalculator:
    def __init__(self, building):
        self.building = building

    def calculate(self):
        return infrastructure_calculation(self.building)
