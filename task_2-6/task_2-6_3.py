donor = input("Введите фенотип группы крови донора (I, II, III, IV): ").strip().upper()
recipient = input("Введите фенотип группы крови пациента (I, II, III, IV): ").strip().upper()
if donor == recipient or donor == "I":
    print(f"Переливание возможно: {donor} -> {recipient}")
else:
    print(f"Переливание теоретически возможно, но не рекомендуется: {donor} -> {recipient}")
