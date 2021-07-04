import React, { useState   } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from "@material-ui/core/AppBar";
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import Background from '../images/documents.png';
import Iesc from '../images/iesc.png';
import Unitbv from '../images/unitbv.png';
const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  title: {
    flexGrow: 1,
    marginLeft:"50px"
  },
  navBarButtons:{
    marginRight:"100px",
    width:"100px"
  },

  firstThird:{
      height: "35%",
      width: "100%",
  },
  firstImag:{
    height: "35%",
    width: "100%",
  },
  secondThird:{
    height: "35%",
    width: "100%",
    backgroundColor: "white",
    marginTop:"-20px",
  },
  thirdThird:{
        height: "30%",
        width: "100%",
        backgroundColor: "black",
        marginTop:"-16px",
        display: "flex", flexDirection: "row", flexWrap: "wrap", alignContent: "center", alignItems: "center", justifyContent: "center" ,
  },
  thirdImag:{
      height:"60%",
      width:"50%",
  },
  paragraph1Second:{
      paddingLeft:"50px"
  },
  paragraph2Second:{
    paddingRight:"50px"
  },
  twoColsSecond:{
    display: "flex", flexDirection: "row", flexWrap: "wrap", alignContent: "center", alignItems: "center", justifyContent:'space-between' ,
  },
  
}));

export default function HomePage() {
    const classes = useStyles();

    return (
      <div className={classes.root}>
        <AppBar position="static">
          <Toolbar>
            <Typography variant="h6" className={classes.title}>
              Blockchainul meu misto
            </Typography>
            <Button color="inherit" className={classes.navBarButtons}>About</Button>
            <Button color="inherit" className={classes.navBarButtons}>Blockchain</Button>
            <Button color="inherit" className={classes.navBarButtons}>Project</Button>
          </Toolbar>
        </AppBar>
        <div className={classes.firstThird}>
            <img src={Background} className={classes.firstImag}/>
        </div>
        <div className={classes.secondThird}>
            <p className={classes.paragraph1Second}>The best blockchain Romania's going to have</p>
            <div className={classes.twoColsSecond} >
                <p className={classes.paragraph1Second}>Build by me ofc</p>
                <p className={classes.paragraph2Second}>Proiect licenta</p>
            </div>
            
        </div>
        <div className={classes.thirdThird}>
            <img src={Iesc} className={classes.thirdImag}/>
            <img src={Unitbv} className={classes.thirdImag}/>
        </div>
      </div>
    );

}