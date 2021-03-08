import { Application } from 'stimulus'
import StimulusReflex from 'stimulus_reflex'
import WebsocketConsumer from 'sockpuppet-js'
import CableReady from 'cable_ready'
import debounced from 'debounced'
import ToDoController from './controllers/todo_controller'

debounced.initialize()
import TurboLinks from 'turbolinks'

TurboLinks.start()

const application = Application.start()
const ssl = location.protocol !== 'https:' ? '' : 's';
const consumer = new WebsocketConsumer(`ws${ssl}://${location.hostname}:${location.port}/ws/sockpuppet-sync`)

consumer.subscriptions.create('ChatChannel', {
  received (data) {
    if (data.cableReady) CableReady.perform(data.operations)
  }
})
 

application.register("todo", ToDoController)
StimulusReflex.initialize(application, { consumer, debug: true })
