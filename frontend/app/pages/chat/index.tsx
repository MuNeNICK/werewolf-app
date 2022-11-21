import { io } from "socket.io-client";
import { useState, useEffect } from 'react'

type ContainerProps = {}

type ChatType = {
  userName: string
  message: string
  datetime: string
}

// フロントと同じサーバならドメインは省略可能
// サーバーサイドで使われているパスを指定

const socket = io("http://192.168.0.221:5000")
const [newChat, setNewChat] = useState<ChatType>()
const [chats, setChats] = useState<ChatType[]>()
useEffect(() => {
  socket.on('connect', () => {
    console.log('socket connected!!')
  })
  socket.on('disconnect', () => {
    console.log('socket disconnected!!')
  })
  socket.on('text_update_request', (newData: ChatType) => {
    console.log('Get Updated Data', newData)
  setNewChat(newData)
  })
  return () => {
    socket.close()
  }
}, [])
useEffect(() => {
  if (newChat.message) {
    setChats([ ...chats, newChat])
  }
}, [newChat])