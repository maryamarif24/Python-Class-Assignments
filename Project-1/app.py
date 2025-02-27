import streamlit as st

# Conversion functions
def length_conversion(value, from_unit, to_unit):
    length_units = {
        "Kilometer (km)": 1, "Meter (m)": 1000, "Centimeter (cm)": 100000, "Millimeter (mm)": 1000000,
        "Mile (mi)": 0.621371, "Yard (yd)": 1093.6133, "Foot (ft)": 3280.84, "Inch (in)": 39370.1
    }
    return value * (length_units[to_unit] / length_units[from_unit])


def temperature_conversion(value, from_unit, to_unit):
    conversions = {
        ("Celsius (°C)", "Fahrenheit (°F)"): lambda x: (x * 9/5) + 32,
        ("Celsius (°C)", "Kelvin (K)"): lambda x: x + 273.15,
        ("Fahrenheit (°F)", "Celsius (°C)"): lambda x: (x - 32) * 5/9,
        ("Fahrenheit (°F)", "Kelvin (K)"): lambda x: (x - 32) * 5/9 + 273.15,
        ("Kelvin (K)", "Celsius (°C)"): lambda x: x - 273.15,
        ("Kelvin (K)", "Fahrenheit (°F)"): lambda x: (x - 273.15) * 9/5 + 32
    }
    return conversions.get((from_unit, to_unit), lambda x: x)(value)


def mass_conversion(value, from_unit, to_unit):
    mass_units = {
        "Kilogram (kg)": 1, "Gram (g)": 1000, "Milligram (mg)": 1000000, "Pound (lb)": 2.20462,
        "Ounce (oz)": 35.274, "Ton (t)": 0.001
    }
    return value * (mass_units[to_unit] / mass_units[from_unit])


def speed_conversion(value, from_unit, to_unit):
    speed_units = {
        "Meter per second (m/s)": 1, "Kilometer per hour (km/h)": 3.6, "Mile per hour (mph)": 2.23694,
        "Foot per second (ft/s)": 3.28084, "Knot (kn)": 1.94384
    }
    return value * (speed_units[to_unit] / speed_units[from_unit])


def time_conversion(value, from_unit, to_unit):
    time_units = {
        "Second (s)": 1, "Minute (min)": 60, "Hour (h)": 3600, "Day (d)": 86400
    }
    return value * (time_units[to_unit] / time_units[from_unit])


def volume_conversion(value, from_unit, to_unit):
    volume_units = {
        "Liter (L)": 1, "Milliliter (mL)": 1000, "Cubic meter (m³)": 0.001,
        "Gallon (gal)": 0.264172, "Pint (pt)": 2.11338
    }
    return value * (volume_units[to_unit] / volume_units[from_unit])


def area_conversion(value, from_unit, to_unit):
    area_units = {
        "Square Kilometer (km²)": 1, "Square Meter (m²)": 1e6, "Square Centimeter (cm²)": 1e10, "Square Millimeter (mm²)": 1e12,
        "Hectare (ha)": 100, "Acre (ac)": 247.105, "Square Mile (mi²)": 0.386102, "Square Yard (yd²)": 1196000,
        "Square Foot (ft²)": 10760000, "Square Inch (in²)": 1550000000
    }
    return value * (area_units[to_unit] / area_units[from_unit])

# Streamlit UI
st.title("🔄 Unit Converter")

conversion_type = st.selectbox("Choose conversion type:", ["Length", "Temperature", "Mass", "Speed", "Time", "Volume", "Area"])

if conversion_type == "Length":
    st.header("📏 Length Conversion")
    units = ["Kilometer (km)", "Meter (m)", "Centimeter (cm)", "Millimeter (mm)", "Mile (mi)", "Yard (yd)", "Foot (ft)", "Inch (in)"]
    converter = length_conversion

elif conversion_type == "Temperature":
    st.header("🌡️ Temperature Conversion")
    units = ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"]
    converter = temperature_conversion

elif conversion_type == "Mass":
    st.header("⚖️ Mass Conversion")
    units = ["Kilogram (kg)", "Gram (g)", "Milligram (mg)", "Pound (lb)", "Ounce (oz)", "Ton (t)"]
    converter = mass_conversion

elif conversion_type == "Speed":
    st.header("🚀 Speed Conversion")
    units = ["Meter per second (m/s)", "Kilometer per hour (km/h)", "Mile per hour (mph)", "Foot per second (ft/s)", "Knot (kn)"]
    converter = speed_conversion

elif conversion_type == "Time":
    st.header("⏳ Time Conversion")
    units = ["Second (s)", "Minute (min)", "Hour (h)", "Day (d)"]
    converter = time_conversion

elif conversion_type == "Volume":
    st.header("🛢️ Volume Conversion")
    units = ["Liter (L)", "Milliliter (mL)", "Cubic meter (m³)", "Gallon (gal)", "Pint (pt)"]
    converter = volume_conversion

elif conversion_type == "Area":
    st.header("📐 Area Conversion")
    units = ["Square Kilometer (km²)", "Square Meter (m²)", "Square Centimeter (cm²)", "Square Millimeter (mm²)",
             "Hectare (ha)", "Acre (ac)", "Square Mile (mi²)", "Square Yard (yd²)", "Square Foot (ft²)", "Square Inch (in²)"]
    converter = area_conversion

# Common UI Elements
value = st.number_input("Enter value:", min_value=0.0, format="%.6f")
from_unit = st.selectbox("From:", units)
to_unit = st.selectbox("To:", units)

if st.button("Convert"):
    result = converter(value, from_unit, to_unit)
    st.success(f"✅ {value} {from_unit} = {result:.6f} {to_unit}")

st.write("📌 Created with ❤️ using Streamlit")
