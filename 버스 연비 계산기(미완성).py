def calculate_mileage(distance, fuel_used):
    try:
        distance = float(distance)
        fuel_used = float(fuel_used)

        if distance <= 0 or fuel_used <= 0:
            raise ValueError("거리와 연료 사용량은 양수여야 합니다.")

        mileage = distance / fuel_used
        return mileage
    except ValueError as e:
        return str(e)

def main():
    print("버스 연비 계산기")
    distance = input("총 주행 거리 (km): ")
    fuel_used = input("사용된 연료 양 (L): ")

    result = calculate_mileage(distance, fuel_used)

    if isinstance(result, float):
        print(f"연비: {result:.2f} km/L")
    else:
        print(f"오류: {result}")

if __name__ == "__main__":
    main()
