"""5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника."""

rev_sum = float(input("Enter revenue amount "))
exp_sum = float(input("Enter expenses amount "))
inc_los_value = rev_sum - exp_sum
if inc_los_value > 0:
    print("Замшелая конторка отработала в плюс. прибыль составила {} у.е, рентабильность выручки {:.3f} у.е."
          .format(rev_sum, inc_los_value/rev_sum))

    employee_number = int(input("Enter number of employees "))
    print("Прибыль в расчете на одного сотрудника: {:.4f}".format(inc_los_value / employee_number))
else:
    print("Конторка идет на дно, как собсвенно и твоя жизнь. Убыток {} у.е."
          .format(exp_sum))
