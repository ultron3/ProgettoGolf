CREATE TABLE `golfclub`.`partecipanti` (
  `id` INT NOT NULL,
  `nome` VARCHAR(45) NULL,
  -- Altre colonne della tabella
  PRIMARY KEY (`id`),
  INDEX `nome_idx` (`nome` ASC) VISIBLE
);


--"UPDATE partecipanti SET punti = %s WHERE cognome = %s"