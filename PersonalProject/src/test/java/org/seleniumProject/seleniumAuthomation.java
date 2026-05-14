package org.seleniumProject;

import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

import java.time.Duration;

public class seleniumAuthomation extends BaseTest{
    @DataProvider(name = "loginData")
    public Object[][] loginData() {
        return new Object[][]{
                {"merr218@gmail.com", "Test@1234"},

        };
    }


    @Test(priority =1 )
    public  void userRegistration() throws InterruptedException {
       // driver.manage().deleteAllCookies();
        driver.get("https://parabank.parasoft.com/parabank/");
        registrationScreen signup = new registrationScreen(driver);
        signup.getRegbtn().click();
        Thread.sleep(5000);
        signup.getFirstName().sendKeys("joel");
        signup.getLastName().sendKeys("paul");
        Thread.sleep(5000);
        signup.getAddress().sendKeys("12 urel street");
        signup.getCity().sendKeys("Ikorodu");
        Thread.sleep(5000);
        signup.getState().sendKeys("Lagos");
        signup.getZipcode().sendKeys("100001");
        Thread.sleep(5000);
        signup.getPhone().sendKeys("08057588945");
        signup.getSsn().sendKeys("5678");
        Thread.sleep(5000);
        signup.getUserName().sendKeys("mikeo6789@gmail.com");
        signup.getPassword().sendKeys("Test@1234");
        Thread.sleep(5000);
        signup.getConfirmPassword().sendKeys("Test@1234");
        Thread.sleep(5000);
        signup.getRegbtnfinal().click();
        String actualText = signup.getAccountCreationAssertion().getText();
        Thread.sleep(5000);
        System.out.println(actualText);
        Assert.assertTrue(actualText.contains("Welcome"));

    }
    @Test(priority = 3, dataProvider = "loginData")
    public void loginTest(String userName, String password) throws InterruptedException {
        driver.get("https://parabank.parasoft.com/parabank/about.htm");
        loginScreen login = new loginScreen(driver);
        Thread.sleep(5000);
        login.getUsernamelogin().sendKeys(userName);
        login.getPasswordlogin().sendKeys(password);
        login.getLoginBtn().click();
    }
    @Test(priority = 2, dependsOnMethods  = "userRegistration")
    public void OpenAccount() throws InterruptedException {
        driver.get("https://parabank.parasoft.com/parabank/");
        openAccountScreen account = new openAccountScreen(driver);
        Thread.sleep(5000);
        account.getOpenNewAcct().click();
        Thread.sleep(300);
       WebElement acctType =  account.getAcctType();
       acctType.click();
       Select select = new Select(acctType);
       select.selectByVisibleText("SAVINGS");
       WebElement Id = account.getAcctId();
       Id.click();
        Select select2 = new Select(Id);
        select2.selectByIndex(0);;
        account.getOpenNewAcctBtn().click();
        account.getLogOut().click();


    }
    @Test(priority = 4)
    public void flightBooking() throws InterruptedException {
        driver.get("https://blazedemo.com/");
        flightBookingScreen bookFlight = new flightBookingScreen(driver);
        WebElement departure = bookFlight.getSelectDeparture();
        departure.click();
        Select select = new Select(departure);
        select.selectByVisibleText("Boston");
        Thread.sleep(5000);

        WebElement Arrival = bookFlight.getSelectArrival();
        Arrival.click();
        Select select1 = new Select(Arrival);
        select1.selectByVisibleText("Rome");
        bookFlight.getSubmitBth().click();
        // WebElement text =bookFlight.getUnitedAirline();
        Assert.assertTrue(true, "United Airlines");
        bookFlight.getChoseFlight().click();
        bookFlight.getName().sendKeys("Jacks Milla");
        bookFlight.getAddress().sendKeys("12, Yoro Street");
        bookFlight.getCity().sendKeys("Villa");
        bookFlight.getState().sendKeys("Abuja");
        Thread.sleep(5000);

        Actions actions = new Actions(driver);
        JavascriptExecutor js = (JavascriptExecutor) driver;
        WebElement zip = bookFlight.getFightNum();
        js.executeScript("arguments[0].scrollIntoView(true);", zip);
        actions.doubleClick(zip).perform();
        actions.keyDown(Keys.CONTROL)
                .sendKeys("c")
                .keyUp(Keys.CONTROL)
                .perform();

        Thread.sleep(4000);
       WebElement zipcode = bookFlight.getZipcode();
        js.executeScript("arguments[0].scrollIntoView(true);", zipcode);
       zipcode.click();
        actions.keyDown(Keys.CONTROL)
                .sendKeys("v")
                .keyUp(Keys.CONTROL)
                .perform();

        WebElement cards = bookFlight.getCardType();
        cards.click();
        Select type = new Select(cards);
        type.selectByVisibleText("American Express");

        bookFlight.getCreditCardNum().sendKeys("120067845");
        bookFlight.getMonth().clear();
        bookFlight.getMonth().sendKeys("12");
        bookFlight.getYear().clear();
        bookFlight.getYear().sendKeys("2028");
        bookFlight.getNameOnCard().sendKeys("Jacks Milla");
        bookFlight.getRememberMe().click();
        bookFlight.getPurchasebtn().click();


    }

    }

