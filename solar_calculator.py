"""
برنامج هندسي لحساب الطاقة الشمسية والجدوى الاقتصادية
التخصص: الهندسة الكهربائية / هندسة الطاقة / الهندسة العامة
المدخلات: القدرة المطلوبة، ساعات الذروة الشمسية، تكلفة kWh، تكلفة التركيب.
المخرجات: الطاقة المنتجة سنوياً، التوفير المالي، وفترة استرداد رأس المال.
"""

def validate_positive_float(prompt_text):
    """التحقق من صحة المدخلات الرقمية وأنها أكبر من الصفر (يتعامل مع المدخلات الخاطئة)."""
    while True:
        try:
            value = float(input(prompt_text))
            if value <= 0:
                print("خطأ: يجب أن تكون القيمة أكبر من الصفر. حاول مرة أخرى.")
                continue
            return value
        except ValueError:
            print("خطأ: يرجى إدخال رقم صحيح أو عشري صالح.")

def calculate_solar_system(capacity_kw, peak_sun_hours, electricity_rate, installation_cost):
    """حساب الطاقة المنتجة، التوفير السنوي، وفترة الاسترداد."""
    # افتراض كفاءة النظام بنسبة 80% (System Performance Ratio)
    system_efficiency = 0.80
    
    daily_energy_kwh = capacity_kw * peak_sun_hours * system_efficiency
    annual_energy_kwh = daily_energy_kwh * 365
    annual_savings_sar = annual_energy_kwh * electricity_rate
    
    # فترة استرداد رأس المال بالسنوات
    payback_period_years = installation_cost / annual_savings_sar if annual_savings_sar > 0 else 0
    
    return {
        "daily_energy": daily_energy_kwh,
        "annual_energy": annual_energy_kwh,
        "annual_savings": annual_savings_sar,
        "payback_period": payback_period_years
    }

def main():
    print("--- نظام تحليل وتقييم مشاريع الطاقة الشمسية الكهروضوئية ---")
    
    # إدخال البيانات مع التحقق من الأخطاء
    capacity_kw = validate_positive_float("أدخل سعة النظام المقترحة بالكيلوواط (kW, مثال: 10): ")
    peak_sun_hours = validate_positive_float("أدخل متوسط ساعات الذروة الشمسية يومياً (الساعات, مثال: 5.5): ")
    electricity_rate = validate_positive_float("أدخل سعر استهلاك الكهرباء لكل كيلوواط-ساعة (ريال/kWh, مثال: 0.18): ")
    installation_cost = validate_positive_float("أدخل التكلفة الإجمالية لتركيب النظام (ريال, مثال: 35000): ")
    
    # إجراء الحسابات الهندسية
    results = calculate_solar_system(capacity_kw, peak_sun_hours, electricity_rate, installation_cost)
    
    # عرض النتائج مع الوحدات المعقولة
    print("\n" + "="*40)
    print("نتائج التحليل الهندسي والاقتصادي:")
    print("="*40)
    print(f"1. الطاقة المنتجة يومياً: {results['daily_energy']:.2f} kWh")
    print(f"2. الطاقة المنتجة سنوياً: {results['annual_energy']:.2f} kWh")
    print(f"3. التوفير المالي السنوي المتوقع: {results['annual_savings']:.2f} SAR")
    print(f"4. فترة استرداد رأس المال (Payback Period): {results['payback_period']:.2f} سنوات")
    print("="*40)

if __name__ == "__main__":
    main()