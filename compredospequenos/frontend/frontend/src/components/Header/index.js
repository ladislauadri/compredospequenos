import React from 'react';
import {
  makeStyles,
  AppBar,
  Toolbar,
  IconButton,
  Button,
  Switch,
} from '@material-ui/core';
import clsx from 'clsx';
import { useTheme } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import MenuIcon from '@material-ui/icons/Menu';
import AccountCircle from '@material-ui/icons/AccountCircle';
import Brightness5Icon from '@material-ui/icons/Brightness5';
import Brightness3Icon from '@material-ui/icons/Brightness3';

import Apps from '@material-ui/icons/Apps';
import MoreVert from '@material-ui/icons/MoreVert';


const drawerWidth = 300;



const useStyles = makeStyles((theme) => ({
    root: {
        height: '100%',
        minHeight: '100vh',
        backgroundColor: theme.palette.background.dark,
      },
      logo: {
        height: 70,
      },
      drawer: {
        width: drawerWidth,
        flexShrink: 0,
        whiteSpace: 'nowrap',
      },
      drawerPaper: {
        width: 240,
        borderRight: 'none',
    },
    drawerOpen: {
      width: drawerWidth,
      transition: theme.transitions.create('width', {
        easing: theme.transitions.easing.sharp,
        duration: theme.transitions.duration.enteringScreen,
      }),
    },
    drawerClose: {
      transition: theme.transitions.create('width', {
        easing: theme.transitions.easing.sharp,
        duration: theme.transitions.duration.leavingScreen,
      }),
      overflowX: 'hidden',
      width: theme.spacing(0) + 1,
      [theme.breakpoints.up('sm')]: {
        width: theme.spacing(12) + 1,
      },
    },
      menuIcon: {
        paddingRight: theme.spacing(5),
        paddingLeft: theme.spacing(6),
      },
      icons: {
        paddingRight: theme.spacing(5),
      },
      grow: {
        flexGrow: 1,
      },
      listItemText: {
        fontSize: 14,
      },
      listItem: {
        paddingTop: 4,
        paddingBottom: 4,
      },
      subheader: {
        textTransform: 'uppercase',
      },
  appBar: {
    zIndex: theme.zIndex.drawer + 1,
    transition: theme.transitions.create(['width', 'margin'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
  },
  appBarShift: {
    marginLeft: drawerWidth,
    width: `calc(100% - ${drawerWidth}px)`,
    transition: theme.transitions.create(['width', 'margin'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
  },
  menuButton: {
    marginRight: 36,
  },
  hide: {
    display: 'none',
  },
  toolbar: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'flex-end',
    padding: theme.spacing(0, 1),
    // necessary for content to be below app bar
    ...theme.mixins.toolbar,
  },
  content: {
    flexGrow: 1,
    padding: theme.spacing(3),
    marginLeft: '50px',
    marginRight: '50px',
  },
}));

export default function Header({ darkMode, setDarkMode }) {
  const classes = useStyles();
  const theme = useTheme();
  const [open, setOpen] = React.useState(false);

  const handleDrawerOpen = () => {
    setOpen(true);
  };

  const handleDrawerClose = () => {
    setOpen(false);
  };

  return (
    <div className={classes.root}>
      <CssBaseline />
      <AppBar
        position="fixed"
        className={clsx(classes.appBar, {
          [classes.appBarShift]: open,
        })}
      >
        <Toolbar>
          <IconButton
            color="inherit"
            aria-label="open drawer"
            onClick={handleDrawerOpen}
            edge="start"
            className={clsx(classes.menuButton, {
              [classes.hide]: open,
            })}
          >
            <MenuIcon />
          </IconButton>
          <img
            src={
              theme.palette.type === 'dark'
                ? '/assets/img/Condominios-e-Vizinhanca-sem-fundo.webp'
                : '/assets/img/Condominios-e-Vizinhanca-sem-fundo.webp'
            }
            alt='logo'
            className={classes.logo}
          />
          <div className={classes.grow} />
          <IconButton className={classes.icons}>
            <Brightness5Icon />
          </IconButton>
          <Switch
            value={darkMode}
            onChange={() => setDarkMode(!darkMode)}
            className={classes.icons}
          />
          <IconButton className={classes.icons}>
            <Brightness3Icon />
          </IconButton>

          <IconButton className={classes.icons}>
            <Apps />
          </IconButton>
          <IconButton className={classes.icons}>
            <MoreVert />
          </IconButton>
          <Button
            startIcon={<AccountCircle />}
            variant='outlined'
            color='secondary'
          >
            Fazer Login
          </Button>
        </Toolbar>
      </AppBar>
    </div>
  );
}