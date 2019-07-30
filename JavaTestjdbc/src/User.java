class User {
  private int id;
  private String name,adderss,gender,knowledge,subject;
  byte[] picture;

    public User(int id, String name, String adderss, String gender, String knowledge, String subject,byte[] picture) {
        this.id = id;
        this.name = name;
        this.adderss = adderss;
        this.gender = gender;
        this.knowledge = knowledge;
        this.subject = subject;
    }

    public int getSno() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getAdderss() {
        return adderss;
    }

    public String getGender() {
        return gender;
    }

    public String getKnowledge() {
        return knowledge;
    }

    public String getSubject() {
        return subject;
    }
    public byte[] getPicture(){
        return picture;
    }
  
}
/*
 try {
            Class.forName("com.mysql.jdbc.Driver");
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/testjdbc", "root", "");
            int row = jTableContent.getSelectedRow();
            String value = (jTableContent.getModel().getValueAt(row, 0).toString());
            String query = "UPDATE sfjava SET name=?,address=?,gender=?,knowledge=?,subject=? WHERE id " + value;
            PreparedStatement pst = con.prepareStatement(query);
            pst.setString(1, txtUsername.getText());
            pst.setString(2, txtAddress.getText());
            //RADIOBOX CONFIGERATION
            if (rdmale.isSelected()) {
                gender = "Male";
            }
            if (rdfemale.isSelected()) {
                gender = "Female";
            }
            pst.setString(3, gender);

            //CHECKBOX CONFIGURETION 
            if (chkjava.isSelected()) {
                knowledge += chkjava.getText() + " ";
            }
            if (chkpython.isSelected()) {
                knowledge += chkpython.getText() + " ";
            }
            pst.setString(4, knowledge);
            //COMBO CONFIGURATION
            String course;
            course = combsubject.getSelectedItem().toString();
            pst.setString(5, course);

            pst.executeUpdate();
            JOptionPane.showMessageDialog(null, "Insertion successful");
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, e);
        }
    }                                         

    private void jTableContentMouseClicked(java.awt.event.MouseEvent evt) {                                           
        int i = jTableContent.getSelectedRow();
        TableModel model = jTableContent.getModel();
        txtUsername.setText(model.getValueAt(i, 1).toString());
        txtAddress.setText(model.getValueAt(i, 2).toString());
        String sex = model.getValueAt(i, 3).toString();
        if (sex.equals(rdmale)) {
            rdmale.setSelected(true);
        }
        if (sex.equals(rdfemale)) {
            rdfemale.setSelected(true);
        }
        String knowledge = model.getValueAt(i, 4).toString();
        switch (knowledge) {
            case "java ":
                chkjava.setSelected(true);
                chkpython.setSelected(false);
                break;
            case "python":
                chkjava.setSelected(false);
                chkpython.setSelected(true);
                break;
            default:
                chkjava.setSelected(true);
                chkpython.setSelected(true);
                break;
        }
*/