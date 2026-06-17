#!/usr/bin/env python3
"""
MealBot Code - Gestion et optimisation des repas pour la prise de masse
"""


def calculate_calories(proteins: float, carbs: float, fats: float) -> float:
    """
    Calcule le total calorique d'un repas.
    
    Args:
        proteins: Grammes de protéines (1g = 4 kcal)
        carbs: Grammes de glucides (1g = 4 kcal)
        fats: Grammes de lipides (1g = 9 kcal)
    
    Returns:
        Total calorique en kcal
    """
    return (proteins * 4) + (carbs * 4) + (fats * 9)


def calculate_macros_from_calories(total_calories: float, protein_ratio: float = 0.3,
                                    carb_ratio: float = 0.5, fat_ratio: float = 0.2) -> dict:
    """
    Calcule la répartition des macros à partir d'un total calorique.
    
    Args:
        total_calories: Objectif calorique total
        protein_ratio: Ratio de protéines (0-1)
        carb_ratio: Ratio de glucides (0-1)
        fat_ratio: Ratio de lipides (0-1)
    
    Returns:
        Dictionnaire avec les grammes de chaque macro
    """
    macros = {
        'proteins': (total_calories * protein_ratio) / 4,
        'carbs': (total_calories * carb_ratio) / 4,
        'fats': (total_calories * fat_ratio) / 9
    }
    return macros


if __name__ == "__main__":
    # Exemple d'utilisation
    print("MealBot - Calculateur nutritionnel")
    print("-" * 40)
    
    # Calcul simple
    calories = calculate_calories(150, 200, 50)
    print(f"Repas: 150g protéines, 200g glucides, 50g lipides = {calories:.0f} kcal")
    
    # Calcul de macros
    macros = calculate_macros_from_calories(2500)
    print(f"\nPour 2500 kcal (30% protéines, 50% glucides, 20% lipides):")
    print(f"  Protéines: {macros['proteins']:.0f}g")
    print(f"  Glucides: {macros['carbs']:.0f}g")
    print(f"  Lipides: {macros['fats']:.0f}g")
