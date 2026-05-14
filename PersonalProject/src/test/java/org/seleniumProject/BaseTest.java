package org.seleniumProject;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;

import java.time.Duration;

public class BaseTest {


    WebDriver driver;

    @BeforeClass
    public void openUrl() {
        System.setProperty("webdriver.chromedriver","C:\\Users\\Francisca\\Testify-Automation_School\\Module4D\\src\\geckodriver.exe");
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--incognito");
        options.addArguments("--start-maximized");
        driver = new ChromeDriver(options);
        driver.manage().window().maximize();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(100));

    }

    @AfterClass
    public void closeBrowser() {
            driver.quit();

    }
}
