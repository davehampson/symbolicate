# README #


### Symbolicate ###

* How to use:

```
D:\chout>git clone https://github.com/davehampson/symbolicate.git
D:\chout>cd symbolicate
D:\chout\symbolicate>symbolicate.bat -c c:\Users\dave\Downloads\crash.txt -l e:\Unity535p2\Editor\Data\PlaybackEngines\AndroidPlayer\Variations\mono\Release\Symbols\armeabi-v7a\libunity.sym.so

05-26 18:06:51.501: I/DEBUG(242): backtrace:
05-26 18:06:51.501: I/DEBUG(242):     #00  pc 006d4960  /data/app-lib/com.contoso.g-1/libunity.so StateMachineBehaviourPlayer::FireStateMachineBehaviour(int, int, mecanim::statemachine::StateMachineMessage) const at ??:?
05-26 18:06:51.501: I/DEBUG(242):     #01  pc 006d4c0c  /data/app-lib/com.contoso.g-1/libunity.so AnimationPlayable::Destroy(mecanim::memory::MecanimAllocator&) at ??:?
05-26 18:06:51.501: I/DEBUG(242):     #02  pc 006d4c0c  /data/app-lib/com.contoso.g-1/libunity.so AnimationPlayable::Destroy(mecanim::memory::MecanimAllocator&) at ??:?
05-26 18:06:51.501: I/DEBUG(242):     #03  pc 006d4c0c  /data/app-lib/com.contoso.g-1/libunity.so AnimationPlayable::Destroy(mecanim::memory::MecanimAllocator&) at ??:?
05-26 18:06:51.501: I/DEBUG(242):     #04  pc 006d4c0c  /data/app-lib/com.contoso.g-1/libunity.so AnimationPlayable::Destroy(mecanim::memory::MecanimAllocator&) at ??:?
05-26 18:06:51.501: I/DEBUG(242):     #05  pc 001c5510  /data/app-lib/com.contoso.g-1/libunity.so JobQueue::ScheduleDependencies(JobGroup*, JobInfo*, JobInfo*) at ??:?
05-26 18:06:51.501: I/DEBUG(242):     #06  pc 001c595c  /data/app-lib/com.contoso.g-1/libunity.so JobQueue::Exec(JobInfo*, int, int) at ??:?
05-26 18:06:51.501: I/DEBUG(242):     #07  pc 001c4ec0  /data/app-lib/com.contoso.g-1/libunity.so JobQueue::JobQueue(unsigned int, int, JobQueue::JobQueueFlags, char const*, char const*) at ??:?

...
```