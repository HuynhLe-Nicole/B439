# include <iostream>
# include <string>
# include <cctype>
 using namespace std;

//Function  to check password strength and provide tailored suggestions
pair<string, string> checkPasswordStrength(const string& password) {
    bool hasUpper = false;
    bool hasLower = false;
    bool hasDigit = false;
    bool hasSpecial = false;
    int length = password.length();
    string suggestions = "";

    // Check each character in the password
    for (char ch : password) {
        if (isupper(ch)) hasUpper = true;
        if (islower(ch)) hasLower = true;
        if (isdigit(ch)) hasDigit = true;
        if (!isalnum(ch)) hasSpecial = true; //Non-alphanumeric character are special


    }

    // Evaluate password strength and build suggestions
    int score = 0;
    if (length >= 9) score++;
    else suggestions += "- Your password should be at least 9 characters. \n";

    if(hasUpper) score++;
    else suggestions += "- Add at least one uppercase letter. \n";

    if(hasLower) score++;
    else suggestions += "- Add at least one lowercase letter. \n";

    if(hasDigit) score++;
    else suggestions += "- Add at least one number. \n";

    if(hasSpecial) score++;
    else suggestions += "-Add at least one special character. \n";

    //Determine overall strength
    string strength;
    if (score <= 2) strength=  "Weak";
    else if (score <= 4) strength = "Moderate";
    else strength = "Strong";

    return {strength, suggestions};

}

int main() {
    string password;
    string strength;
    string suggestions;

    //Loop until the password is strong
    do {
        // Prompt user for password
        cout <<"Enter your password: ";
        cin >> password;

        //Check password strength and get tailored suggestions
        tie(strength, suggestions) = checkPasswordStrength(password);

        //Display result
        cout << "Your password strength is: " << strength << endl;

        //Provide suggestion if the password is not strong
        if (strength != "Strong") {
            cout << "Your password is not strong enough. Please try again." << endl;
            cout << "Suggestions to improve your password: "<< endl;
            cout << suggestions; // Display tailored suggestions

            cout << "------------------------------------------------------" << endl;
        }
    } while (strength != "Strong") ; //Repeat until the password is strong

    cout << "Congratulation! Your password is good." << endl;

    return 0;

}

