Feature: Sign in user
    Users should have possibility to sign in with OAuth2 providers:
    Google, Facebook, Twitter
    User account should be prefilled with data from corresponding provider

    Scenario: Fail test - try to signup with undefined provider
        Given I have selected to sign up with undefined
        When I try to login
        Then I got response code 404

    Scenario Outline: Sign up user using OAuth2 provider
        Given I have selected to sign up with <provider>
        And I have received provider credentials by submitting login <login> and password <password> to <login_url>
        When I try to login
        And I got response code 302
        And I follow location redirect
        Then I got signed in
        And My profile has name <name> and avatar <userpic>

    Examples:
            | provider | login | password | login_url | name | userpic |
            | Facebook | bill_fikvtrd_fallerwitz@tfbnw.net | 1234567890 | https://www.facebook.com/login.php | Bill Amgaeiijgfdh Fallerwitz | https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-prn3/t1.0-9/10410337_291254401050902_3793840203547307063_n.jpg |
            #            | Twitter  | dummy@dummy.net | 1234567890 | Dummy | https://dummy.net |
            #| Google   | dummy@dummy.net | 1234567890 | Dummy | https://dummy.net |
