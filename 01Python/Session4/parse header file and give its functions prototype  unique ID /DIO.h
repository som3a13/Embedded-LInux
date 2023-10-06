/*
 * DIO.h
 *
 * Created: 9/16/2023 4:46:32 PM
 *  Author: Mohamed Ismail
 */ 
#ifndef DIO_H_
#define DIO_H_
//PINS Configuration
void DIO_setpinDir(char port,char pin,char dir);
void DIO_writePin(unsigned char port,unsigned char pin,unsigned char state);
void DIO_TogglePin(unsigned char port ,unsigned char pin);
unsigned char DIO_ReadPin(unsigned char port ,unsigned char pin);
//PORTS Configuration
void DIO_setportDir(unsigned char port,unsigned char dir);
void DIO_writePort(unsigned char port,unsigned char state);
void DIO_TogglePort(unsigned char port );
unsigned char DIO_ReadPort(unsigned char port);
void DIO_connectpullup(char portname ,char pinnumber, char connect_pullup);
void write_low_nibble(unsigned char portname,unsigned char value);
void write_high_nibble(unsigned char portname,unsigned char value);
#endif /* DIO_H_ */