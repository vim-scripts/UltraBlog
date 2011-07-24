#!/usr/bin/env python

class UBEventQueue:
    queue = []
    listeners = []

    @staticmethod
    def fireEvent(evt):
        UBEventQueue.queue.append(evt)

    @staticmethod
    def processEvents():
        for evt in UBEventQueue.queue:
            for listener in UBEventQueue.listeners:
                if listener.isTarget(evt):
                    UBEventQueue.queue.remove(evt)
                    listener.processEvent(evt)

    @staticmethod
    def registerListener(lsnr):
        UBEventQueue.listeners.append(lsnr)

if __name__ == '__main__':
    pass
