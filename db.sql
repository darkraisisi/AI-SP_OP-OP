SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `huwebshop` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `huwebshop` ;

-- -----------------------------------------------------
-- Table `huwebshop`.`products`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `huwebshop`.`products` ;

CREATE  TABLE IF NOT EXISTS `huwebshop`.`products` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(45) NULL ,
  `gender` VARCHAR(45) NULL ,
  `category` VARCHAR(45) NULL ,
  `brand` VARCHAR(45) NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `huwebshop`.`profiles`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `huwebshop`.`profiles` ;

CREATE  TABLE IF NOT EXISTS `huwebshop`.`profiles` (
  `id` INT NOT NULL ,
  `order_amount` INT NOT NULL DEFAULT 0 ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `huwebshop`.`sessions`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `huwebshop`.`sessions` ;

CREATE  TABLE IF NOT EXISTS `huwebshop`.`sessions` (
  `id` INT NOT NULL ,
  `browser_id` VARCHAR(45) NOT NULL ,
  `segment` VARCHAR(45) NULL ,
  `profiles_id` INT NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_sessions_profiles1_idx` (`profiles_id` ASC) ,
  CONSTRAINT `fk_sessions_profiles1`
    FOREIGN KEY (`profiles_id` )
    REFERENCES `huwebshop`.`profiles` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `huwebshop`.`cart_has_products`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `huwebshop`.`cart_has_products` ;

CREATE  TABLE IF NOT EXISTS `huwebshop`.`cart_has_products` (
  `products_id` INT NOT NULL ,
  `sessions_id` INT NOT NULL ,
  PRIMARY KEY (`products_id`, `sessions_id`) ,
  INDEX `fk_products_has_sessions_sessions1_idx` (`sessions_id` ASC) ,
  INDEX `fk_products_has_sessions_products_idx` (`products_id` ASC) ,
  CONSTRAINT `fk_products_has_sessions_products`
    FOREIGN KEY (`products_id` )
    REFERENCES `huwebshop`.`products` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_products_has_sessions_sessions1`
    FOREIGN KEY (`sessions_id` )
    REFERENCES `huwebshop`.`sessions` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `huwebshop` ;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
