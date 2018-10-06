def __init__(self):
        self.timerController = threading.Event()
        self.timeFeedbackThread = ''
        self.pid = ''
        self.exitStatus = 0
        self.cancelled = 'no'

    def applyPatches(self, repositoryList, loggerName):
        logger = logging.getLogger(loggerName)
        if len(repositoryList) > 1:
            logger.info('Applying patches from repositories ' + ', '.join(repositoryList) + '.')
        else:
            logger.info('Applying patches from repository ' + repositoryList[0] + '.')
        logger.info('The patch repository list was determined to be: ' + str(repositoryList))
        for repository in repositoryList:
            time.sleep(2)
            if 'kernel' in repository.lower():
                # from spUtils import TimeFeedbackThread 
                self.timeFeedbackThread = TimeFeedbackThread(componentMessage='Installing the new kernel', event=self.timerController)
                self.timeFeedbackThread.start()
                command = 'zypper -n --non-interactive-include-reboot-patches --no-refresh in -r ' + repository + ' ' + repository + ':*'
            result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=self.preexec, shell=True)
            self.pid = result.pid
            out, err = result.communicate()
            logger.info('The output of the patch update command (' + command + ') was: ' + out.strip())
            if result.returncode == 0:
                logger.info('Successfully updated the system using patches from the repository ' + repository + '.')
            else:
                self.timeFeedbackThread.stopTimer()
                self.timeFeedbackThread.join()
                print ''
                if self.cancelled == 'yes':
                    logger.info('The patch update was cancelled by the user.')
                    print RED + 'The patch update was cancelled; exiting program execution.' + RESETCOLORS
                else:
                    logger.error('Problems were encountered while updating the system using patches from the repository ' + repository + '.\n' + err)
                    print RED + 'Problems were encountered while applying the patches to the system; check the log file for errors; exiting program execution.' + RESETCOLORS
                self.exitStatus = 1
                return
            self.timeFeedbackThread.stopTimer()
            self.timeFeedbackThread.join()
            print ''

        if len(repositoryList) > 1:
            logger.info('Done applying patches from repositories ' + ', '.join(repositoryList) + '.')
        else:
            logger.info('Done applying patches from repository ' + repositoryList[0] + '.')

    def endTask(self):
        try:
            self.cancelled = 'yes'
            pgid = os.getpgid(self.pid)
            os.killpg(pgid, signal.SIGKILL)
        except OSError:
            pass

    def preexec(self):
        os.setpgrp()

    def getExitStatus(self):
        return self.exitStatus

    def pauseTimerThread(self):
        self.timeFeedbackThread.pauseTimer()

    def resumeTimerThread(self):
        self.timeFeedbackThread.resumeTimer()