package org.example;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class Task2pinterest {
    public static void main(String[] args) {
    System.setProperty("webdriver.Chrome.driver", "C:\\Users\\Francisca\\Testify-Automation_School\\Module4D\\src\\chromedriver.exe");
     //Navigate to url
    WebDriver driver = new ChromeDriver();
    //maximize page
    driver.manage().window().maximize();
    //launch url
    driver.get("https://www.pinterest.com/");
    //driver.close();


}

}
