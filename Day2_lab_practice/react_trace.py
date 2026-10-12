"""ReAct trace for the Smart Agriculture Assistant."""

from day2_tools import get_crop_water


def calculator(expression):
    """Calculate an arithmetic expression."""
    return eval(expression)


print("\n" + "=" * 60)
print("REACT AGENT TRACE")
print("=" * 60)

print("\nQuestion:")
print("""
A farmer has:
- 2 acres of tomato
- 3 acres of rice
- 1 acre of cotton

Find the total water requirement and the water requirement
after a 15% water-saving method.
""")

print("\nThought: I need the water requirement for each crop.")

print("\nAction: get_crop_water('tomato')")
tomato_water = get_crop_water("tomato")
print(f"Observation: {tomato_water} litres/acre")

print("\nAction: get_crop_water('rice')")
rice_water = get_crop_water("rice")
print(f"Observation: {rice_water} litres/acre")

print("\nAction: get_crop_water('cotton')")
cotton_water = get_crop_water("cotton")
print(f"Observation: {cotton_water} litres/acre")

print("\nThought: Now I can calculate the total water requirement.")

expression = (
    f"(2 * {tomato_water}) + "
    f"(3 * {rice_water}) + "
    f"(1 * {cotton_water})"
)

print(f"\nAction: calculator('{expression}')")
total = calculator(expression)
print(f"Observation: {total} litres")

print("\nThought: Now I need to calculate the 15% water saving.")

saving_expression = f"{total} * 0.15"

print(f"\nAction: calculator('{saving_expression}')")
saving = calculator(saving_expression)
print(f"Observation: {saving} litres")

print("\nThought: Subtracting the saved water gives the final requirement.")

final_expression = f"{total} - {saving}"

print(f"\nAction: calculator('{final_expression}')")
final_water = calculator(final_expression)
print(f"Observation: {final_water} litres")

print("\n" + "=" * 60)
print("FINAL ANSWER")
print("=" * 60)

print(f"Total water requirement: {total} litres")
print(f"Water saved: {saving} litres")
print(f"Water requirement after saving: {final_water} litres")