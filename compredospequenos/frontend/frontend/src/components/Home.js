import React, { useEffect, Component, useState   } from 'react';
import {
  makeStyles,
  AppBar,
  Toolbar,
  IconButton,
  Drawer,
  Button,
  List,
  Typography,
  Divider,
  ListItem,
  ListItemIcon,
  ListItemText,

  Switch,
} from '@material-ui/core';
import clsx from 'clsx';
import { useTheme } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import MenuIcon from '@material-ui/icons/Menu';
import ChevronLeftIcon from '@material-ui/icons/ChevronLeft';
import ChevronRightIcon from '@material-ui/icons/ChevronRight';
import InboxIcon from '@material-ui/icons/MoveToInbox';
import MailIcon from '@material-ui/icons/Mail';
import AccountCircle from '@material-ui/icons/AccountCircle';
import Brightness5Icon from '@material-ui/icons/Brightness5';
import Brightness3Icon from '@material-ui/icons/Brightness3';

import Apps from '@material-ui/icons/Apps';
import MoreVert from '@material-ui/icons/MoreVert';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';

import api from '../services/api'
import mime  from 'mime-types';
import ReactPlayer from 'react-player'
import { Waypoint } from 'react-waypoint';
import Avatar from '@material-ui/core/Avatar';
import CardHeader from '@material-ui/core/CardHeader';
import MoreVertIcon from '@material-ui/icons/MoreVert';
import * as moment from 'moment';
import 'moment/locale/pt-br';

import Grid from '@material-ui/core/Grid';










const drawerWidth = 300;

const useStyles = makeStyles((theme) => ({
    root: {
        height: '100%',
        backgroundColor: theme.palette.background,
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
  postItem: {
    backgroundColor: theme.palette.postItem

  }
  
}));



export default function MiniDrawer({ darkMode, setDarkMode }) {
  const classes = useStyles();
  const theme = useTheme();
  const [open, setOpen] = useState(false);
  const [posts, setPosts] = useState([]);
  const [shouldPlay, updatePlayState] = useState(false);

  const handleDrawerOpen = () => {
    setOpen(true);
  };

  const handleDrawerClose = () => {
    setOpen(false);
  };

  useEffect(() => {},[])
  useEffect(() => {
      async function loadPosts() {
          const response = await api.get('posts/?format=json');
          setPosts(response.data)

      }
      loadPosts()
  },[]);
  
    const handleEnterViewport = () => {
      updatePlayState(Boolean(true));
    };
    const handleExitViewport = () => {
      updatePlayState(Boolean(false));
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
                ? '../assets/img/Condominios-e-Vizinhanca-sem-fundo.webp'
                : '../assets/img/Condominios-e-Vizinhanca-sem-fundo.webp'
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
      <Drawer
        variant="permanent"
        className={clsx(classes.drawer, {
          [classes.drawerOpen]: open,
          [classes.drawerClose]: !open,
        })}
        classes={{
          paper: clsx({
            [classes.drawerOpen]: open,
            [classes.drawerClose]: !open,
          }),
        }}
      >
        <div className={classes.toolbar}>
          <IconButton onClick={handleDrawerClose}>
            {theme.direction === 'rtl' ? <ChevronRightIcon /> : <ChevronLeftIcon />}
          </IconButton>
        </div>
        <Divider />
        <List>
          {['Inbox', 'Starred', 'Send email', 'Drafts'].map((text, index) => (
            <ListItem button key={text}>
              <ListItemIcon>{index % 2 === 0 ? <InboxIcon /> : <MailIcon />}</ListItemIcon>
              <ListItemText primary={text} />
            </ListItem>
          ))}
        </List>
        <Divider />
        <List>
          {['All mail', 'Trash', 'Spam'].map((text, index) => (
            <ListItem button key={text}>
              <ListItemIcon>{index % 2 === 0 ? <InboxIcon /> : <MailIcon />}</ListItemIcon>
              <ListItemText primary={text} />
            </ListItem>
          ))}
        </List>
      </Drawer>
      <main className={classes.content}>
        <div className={classes.toolbar} />
         {posts.map(post => {
             console.log(mime.lookup(post.content))
             if( mime.lookup(post.content) === 'video/mp4')
             return (
              <div className={'postItem'} key={post.id}>
                <div className={'postOwner'} > 
                  <div className={'postAvatar'} style={{backgroundImage:`url(${post.username.image})`,}}></div>
                  <div>
                  <p className={'postAuthorName'}>{post.username.firstName +' ' + post.username.lastName}</p>
                  <p className={'postDate'}>{moment(post.createdAt).locale('pt-br').format('LLLL')}</p>

                  </div>
                </div>
                  <div>
                  <Waypoint 

                    onEnter={handleEnterViewport}
                    onLeave={handleExitViewport}
                    >
                    <div style={{height:"100%"}} > 
                    <ReactPlayer 
                    url={post.content} 
                    loop = {true}
                    muted = {true}
                    controls = {true}
                    playing = {shouldPlay}



                    />
                    </div>
                    </Waypoint>
                  </div>
                
                </div>
              )
              if( mime.lookup(post.content) === 'image/png')
              return (
               <div className={'postItem'} key={post.id}>
                 <div className={'postOwner'} > 
                   <div className={'postAvatar'} style={{backgroundImage:`url(${post.username.image})`,}}></div>
                   <div>
                   <p className={'postAuthorName'}>{post.username.firstName +' ' + post.username.lastName}</p>
                   <p className={'postDate'}>{moment(post.createdAt).locale('pt-br').format('LLLL')}</p>
 
                   </div>
                 </div>
                   <div>
                   <img 
                     src={post.content} 
                     alt = {post.description}
                     className={'imgResponsive'}

                     />
                     </div>

                 
                 </div>
               )
     })}

         
      </main>
    </div>
  );
}