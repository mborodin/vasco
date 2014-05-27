Feature: Sign up user
    Users should have possibility to sign up with OAuth2 providers:
    Google, Facebook, Twitter
    User account should be prefilled with data from corresponding provider

    Scenario: Fail test - try to signup with undefined provider
        Given I have selected to sign up with undefined
        When I submit login dummy and password dummy
        Then I got response code 404

    Scenario Outline: Sign up user using OAuth2 provider
        Given I have selected to sign up with <provider>
        When I submit login <login> and password <password>
        Then I got signed up and user profile is created with name <name> and profile picture <userpic>

    Examples:
            | provider | login | password | name | userpic |
            | Facebook | linda_wvapiqk_panditsky@tfbnw.net | 1234567890 | Linda Amdiijcceife Panditsky | https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-prn2/t1.0-9/10410337_291254401050902_3793840203547307063_n.jpg |
            | Twitter  | dummy@dummy.net | 1234567890 | Dummy | https://dummy.net |
            | Google   | dummy@dummy.net | 1234567890 | Dummy | https://dummy.net |
