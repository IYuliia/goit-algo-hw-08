1. Є декілька мережевих кабелів різної довжини, їх потрібно об'єднати по два за раз в один кабель, використовуючи з'єднувачі, у порядку, який призведе до найменших витрат. Витрати на з'єднання двох кабелів дорівнюють їхній сумі довжин, а загальні витрати дорівнюють сумі з'єднання всіх кабелів.

Завдання полягає в тому, щоб знайти порядок об'єднання, який мінімізує загальні витрати.

2. Дано k відсортованих списків цілих чисел. Ваше завдання — об'єднати їх у один відсортований список. Тепер при виконанні завдання ви повинні використати мінімальну купу для ефективного злиття кількох відсортованих списків в один відсортований список. Реалізуйте функцію merge_k_lists, яка приймає на вхід список відсортованих списків та повертає відсортований список.

Приклад очікуваного результату:

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)

Виведення:

Відсортований список: [1, 1, 2, 3, 4, 4, 5, 6]

