# Bullet Journal

## Install

```
pip3 install bullet_journal
```

## Usage

### Remote tools

* Sign up
```
bj signup
```

* Log in
```
bj login
```

* Log out
```
bj logout
```

* Push local updates to remote server
```
bj push
```

* Pull remote updates to local server
```
bj pull
```

### Local tools

* Show all the tasks of a specific day
```
bj daily_log [date]
date: optional argument in the format of yyyy_mm_dd
      default is today
```

* Add to-do task
```
bj add [date]
date: optional argument in the format of yyyy_mm_dd
      default is today
```

* Delete to-do task
```
bj delete [date]
date: optional argument in the format of yyyy_mm_dd
      default is today
```

* Close to-do task
```
bj close [date]
date: optional argument in the format of yyyy_mm_dd
      default is today
```

* Migrate to-do task to a new date
```
bj migrate [date]
date: optional argument in the format of yyyy_mm_dd
      this is the date where the task currently belongs to
      default is today
```
