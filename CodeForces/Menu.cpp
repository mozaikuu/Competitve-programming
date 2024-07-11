#include <iostream>

int choice = 0, count = 0, coffee = 0, tea = 0, hot_chocolate = 0, total = 0;

int rerun()
{
    std::cout << "Would you like anything else?\n";
    std::cout << "\t1. Check cart?\n";
    std::cout << "\t2. add more\n";
    std::cout << "\t3. Quit\n";
    std::cin >> choice;
    return choice;
}

void Menu()
{
    std::cout << "Please select an option: \n\n";

    std::cout << "\t1. Coffee '2L.E'\n";
    std::cout << "\t2. Tea '1L.E'\n";
    std::cout << "\t3. Hot Chocolate '3L.E'\n";
    std::cout << "\t4. Quit\n";

    std::cout << "\n\n";

    std::cin >> choice;

    switch (choice)
    {
    case 1:
        std::cout << "You chose Coffee\n";
        break;
    case 2:
        std::cout << "You chose Tea\n";
        break;
    case 3:
        std::cout << "You chose Hot Chocolate\n";
        break;
    case 4:
        std::cout << "You chose to quit\n";
        break;
    default:
        std::cout << "Invalid choice\n";
        break;
    }

    if (choice == 1)
    {
        std::cout << "How many cups of coffee would you like?\n";
        std::cin >> count;
        coffee = count;
        total += coffee * 2;
    }
    else if (choice == 2)
    {
        std::cout << "How many cups of tea would you like?\n";
        std::cin >> count;
        tea += count;
        total += tea * 1;
    }
    else if (choice == 3)
    {
        std::cout << "How many cups of hot chocolate would you like?\n";
        std::cin >> count;
        hot_chocolate += count;
        total += hot_chocolate * 3;
    }
    else if (choice == 4)
    {
        std::cout << "Thank you for visiting TheBreweryShop\n";
        return;
    }

    rerun();

    if (choice == 1)
    {
        std ::cout << "You have " << coffee << " cups of coffee\n";
        std ::cout << "You have " << tea << " cups of tea\n";
        std ::cout << "You have " << hot_chocolate << " cups of hot chocolate\n";
        std ::cout << "Your total is " << total << " L.E\n\n";
        rerun();
    }
    else if (choice == 2)
    {
        Menu();
    }
    else if (choice == 3)
    {
        std::cout << "That will be " << total << " L.E\n";
        std::cout << "Thank you for visiting TheBreweryShop\n";
        return;
    }
}