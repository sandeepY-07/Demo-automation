Feature: Contact Functionality

    Scenario: Send contact message

        Given user clicks contact menu
        When user enters contact email "test@gmail.com"
        And user enters contact name "Sandeep"
        And user enters message "Testing contact module"
        And user clicks send message button
        Then contact message should be sent successfully