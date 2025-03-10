# PassengerId, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked
# SibSp = Sib( siblings=irmaos/irmas ) | Sp( spouses=conjuges )
# Parch = Par( parents=pais ) | ch( children=filhos ) = parents/children

create database if not exists titanit;
create table if not exists passengers(
  id int primary key auto_increment,
  p_class int unsigned,
  p_name varchar(50) not null,
  p_sex enum('male', 'female') not null,
  p_age int unsigned,
  p_sib_sp int unsigned default 0,
  p_parch int unsigned default 0,
  p_ticket varchar(30) not null,
  p_fare float,
  p_cabin varchar(40) default null,
  embarked enum('S', 'Q', 'C')
);

